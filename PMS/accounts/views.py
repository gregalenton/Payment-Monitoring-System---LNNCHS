from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render, redirect
from . import forms
from .models import Student
from funds.models import Due, Receipt


class IndexView(generic.TemplateView):
    template_name = 'accounts/homepage.html'

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated():
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
        return render(request, self.template_name, context)


class AdminView(generic.TemplateView):
    template_name = 'accounts/homepageadmin.html'


class StudentView(generic.TemplateView):
    template_name = 'accounts/studenthomepage.html'


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
                login(self.request, user)
                return HttpResponseRedirect(reverse('accounts:Student'))
            else:
                return HttpResponse("Account disabled.")    
        else:
            return HttpResponseRedirect(reverse('accounts:Index'))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse('accounts:Index'))


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect(reverse('account:Index'))


class AddStudentView(generic.CreateView):
    template_name = 'accounts/addstudents.html'
    form_class = forms.AddStudentForm

    def form_valid(self, form):
        form.save()
        due = Due.objects.all()
        total = 0

        if len(due) > 0:
            for d in due:
                total = d.cost + total

        Student.toPay = total
        return HttpResponseRedirect(reverse('accounts:Admin'))

    def form_invalid(self, form):
        print form.errors
        return HttpResponseRedirect(reverse('accounts:AddStudent'))
    
class ViewAllStudents(generic.ListView):
    template_name = 'accounts/viewallstudents.html'

    def get_queryset(self):
        queryset = Student.objects.filter(year=7)
        # if self.request.GET.get("browse"):
        #     selection = self.request.GET.get("browse")
        #     if selection == "Cats":
        #         queryset = Cats.objects.all()
        #     elif selection == "Dogs":
        #         queryset = Dogs.objects.all()
        #     elif selection == "Worms":
        #         queryset = Worms.objects.all()
        #     else:
        #         queryset = Cats.objects.all()
        print queryset
        return queryset

#class StudentView():