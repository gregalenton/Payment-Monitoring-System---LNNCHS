from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from . import forms


class IndexView(generic.TemplateView):
    template_name = 'accounts/homepage.html'


class AdminView(generic.TemplateView):
    template_name = 'accounts/homepageadmin.html'


class AdminStudents(generic.TemplateView):
    template_name = 'accounts/students.html'


class AdminLoginView(generic.FormView):
    form_class = forms.AdminLoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

            return HttpResponseRedirect(reverse('accounts:Admin'))
        else:
            return super(AdminLoginView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('accounts:Index'))


class StudentLoginView(generic.FormView):
    form_class = forms.StudentLoginForm

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['student_ID'],
                            password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)

            return HttpResponseRedirect(reverse(''))
        else:
            return super(StudentLoginView, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponseRedirect('accounts:Index')


class AddStudentView(generic.CreateView):
    template_name = 'accounts/addstudents.html'
    form_class = forms.AddStudentForm

    

#class AllStudents():


#class StudentView():