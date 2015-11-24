from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.views import generic
from . import forms
from django.core.urlresolvers import (reverse_lazy, reverse)
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))


def user_login(request):
    if request.user.is_authenticated():
        return render_to_response('accounts/homepage-admin.html')
    else:
        context = RequestContext(request)

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render_to_response('accounts/homepage-admin.html', {}, context)
                else:
                    return HttpResponse("Account disabled.")
            else:
            
                print "Invalid login details: {0}, {1}".format(username, password)
                return HttpResponse("Invalid login details supplied.")
        else:

            return render_to_response('accounts/login.html', {}, context)


class HomeView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('accounts/home.html', {}, {})


class AdminHomeView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('accounts/homepage-admin.html')


class LogoutView(LoginRequiredMixin, generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class AddStudentView(LoginRequiredMixin, generic.CreateView):

    template_name = 'accounts/add_student.html'
    form_class = forms.AddStudentForm

    def form_valid(self, form):
        return super(AddStudentView, self).form_valid(form)

    def get_success_url(self):
 
        return reverse('accounts:home')


class EditStudentView(LoginRequiredMixin, generic.UpdateView):
    model = models.StudentInfo
    template_name = 'accounts/edit_student.html'
    fields = ['student_lastname', 'student_firstname', 'student_middlename',
              'student_birthday', 'student_year', 'student_section',
              'student_gender', 'student_address', 'student_guardian',
              'student_guardian_contact', 'student_guardian_address', 'student_scholarship',
              'student_sibling', 'student_bandMem', 'student_paid', 'student_toPay']


    def get_success_url(self):
        return reverse('accounts:home')

    def get_context_data(self, **kwargs):

        context = super(EditStudentView, self).get_context_data(**kwargs)
        context['action'] = reverse('accounts:editstudent',
                                    kwargs={'pk': self.get_object().student_id})

        return context



# def EditStudentView(request):
#     if 'input' in request.GET and request.GET['input']:
#         inp = request.GET['input']
#         student = models.StudentInfo.objects.get(pk=inp)
#         form = forms.EditStudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             # student.save()
#             return HttpResponseRedirect('/accounts/home/')
#         else:   
#             return render(request, 'accounts/edit_student.html', {'form': form})
#             #return HttpResponse("hoy")
#     else:
#         return HttpResponseRedirect('/accounts/displaysearchresults/')



class SearchStudentView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('accounts/search_student.html') 


    def StudentInfoView(request):
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            student = models.StudentInfo.objects.get(student_lastname=inp)
            return render(request, 'accounts/view_studentinfo.html',
                {'student': student, 'query': inp})
        else:
            return HttpResponseRedirect('/accounts/displaysearchresults/')   



def DisplaySearchResults(request):
    if 'input' in request.GET and request.GET['input']:
        inp = request.GET['input']
        students = models.StudentInfo.objects.filter(student_lastname=inp)
        return render(request, 'accounts/search_student_result.html',
            {'students': students, 'query': inp})
    else:
        return HttpResponseRedirect('/accounts/searchstudent/')

# class DisplaySearchResults(LoginRequiredMixin, generic.View):
#     def get(self, request):
#         if 'input' in request.GET and request.GET['input']:
#             inp = request.GET['input']
#             students = models.StudentInfo.objects.filter(student_lastname=inp)
#             return render(request, 'accounts/search_student_result.html',
#                 {'students': students, 'query': inp})
#         else:
#             return HttpResponseRedirect('/accounts/searchstudent/')

