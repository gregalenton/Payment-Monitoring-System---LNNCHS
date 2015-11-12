from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.views import generic
from . import forms
from django.core.urlresolvers import (reverse_lazy, reverse)
from django.contrib.auth.decorators import login_required

def index(request):
    return render_to_response('accounts/index.html', {}, {})


def admin_home(request):
    if request.user.is_authenticated():
        return render_to_response('accounts/homepage-admin.html')
    else:
        return HttpResponseRedirect('/')

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


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))

class AddStudentView(LoginRequiredMixin,generic.CreateView):

    template_name = 'accounts/add_student.html'
    form_class = forms.AddStudentForm

    def form_valid(self,form):
        return super(AddStudentView,self).form_valid(form)


    def get_success_url(self):
        return reverse('accounts:index')