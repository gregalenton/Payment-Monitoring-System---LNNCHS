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
        return HttpResponseRedirect(reverse('accounts:Admin'))

    def form_invalid(self, form):
        # print form.firstname
        print "Invalid!"
        print form.errors
        return HttpResponseRedirect(reverse('accounts:AddStudent'))
    # def post(self, request, *args, **kwargs):
    #     context = self.get_context_data(request)
    #     return super(AddStudentView, self).render_to_response(context)

    # def get_context_data(self, request, **kwargs):
    #     context = super(AddStudentView, self).get_context_data()
    #     form = forms.AddStudentForm(self.request.POST)
    #     context['form'] = form

    #     firstname = request.POST.get('firstname', '')
    #     lastname = request.POST.get('lastname', '')
    #     year = request.POST.get('year', '')
    #     section = request.POST.get('section', '')
    #     address = request.POST.get('address', '')
    #     gfirstname = request.POST.get('gfirstname', '')
    #     gaddress = request.POST.get('gaddress', '')
    #     gcontact = request.POST.get('gcontact', '')
    #     band_member = request.POST.get('band_member', '')
    #     sibling = request.POST.get('sibling', '')
    #     scholarship = request.POST.get('scholarship', '')
    #     print firstname
    #     print lastname
    #     print year
    #     print section
    #     print address
    #     print gfirstname
    #     print gaddress
    #     print gcontact
    #     print band_member
    #     print sibling
    #     print scholarship

    #     if form.is_valid():
    #         form.save(commit = True)

    #     return context

class ViewAllStudents(generic.ListView):
    template_name = 'accounts/viewallstudents.html'

#class StudentView():