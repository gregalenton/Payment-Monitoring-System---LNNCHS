from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render, redirect
from . import forms


class IndexView(generic.TemplateView):
    template_name = 'accounts/homepage.html'

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated():
            # print "Inside1"
            return HttpResponseRedirect(reverse('accounts:Admin'))
        
        context = {
            'user': request.user,
            'page_title': 'Welcome!',
        }
        if request.user and not request.user.is_anonymous():
            context = {
                'page_title': 'Welcome ' +
                str(request.user.get_full_name()),
            }
        # print "Inside2"
        return render(request, self.template_name, context)

class AdminView(generic.TemplateView):
    template_name = 'accounts/homepageadmin.html'


class AdminStudents(generic.TemplateView):
    template_name = 'accounts/students.html'


class AdminLoginView(generic.FormView):
    form_class = forms.AdminLoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            if user.is_active:
                login(self.request, user)
                return HttpResponseRedirect(reverse('accounts:Admin'))
            else:
                return HttpResponse("Account disabled.")    
        else:
            return HttpResponseRedirect(reverse('accounts:Index'))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('accounts:Index'))


class StudentLoginView(generic.FormView):
    form_class = forms.StudentLoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            if user.is_active:
                print "Inside"
                login(self.request, user)
                return HttpResponse("This is for the Student's Login View")
                # return HttpResponseRedirect(reverse('accounts:Students'))
                
            else:
                return HttpResponse("Account disabled.")    
        else:
            return HttpResponseRedirect(reverse('accounts:Index'))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('accounts:Index'))
        # return HttpResponse("Invalid!")


def user_logout(request):
        if request.user.is_authenticated():
            logout(request)
            return HttpResponseRedirect(reverse('account:Index'))


class AddStudentView(generic.CreateView):
    template_name = 'accounts/addstudents.html'
    form_class = forms.AddStudentForm

    def form_valid(self, form):
        return super(AddStudentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:Admin')



#class AllStudents():


#class StudentView():