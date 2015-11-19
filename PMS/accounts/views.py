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
        return reverse('accounts:index')


# class EditStudentView(LoginRequiredMixin, generic.UpdateView):
    
#     template_name = 'accounts/edit_student.html'
#     form_class = forms.EditStudentForm


def EditStudentView(request):
    if 'input' in request.GET and request.GET['input']:
        inp = request.GET['input']
        student = models.StudentInfo.objects.get(pk=inp)
        form = forms.EditStudentForm(instance=student, data=request.POST)
        if form.is_valid():
            form.save()
            student.save()
            return render_to_response('accounts/successful_edit.html')
        else:   
            return render(request, 'accounts/edit_student.html', {'form': form})
    else:
        return HttpResponseRedirect('/accounts/displaysearchresults/')


class SearchStudentView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('accounts/search_student.html') 


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

