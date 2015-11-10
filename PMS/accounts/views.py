from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from forms import AddStudentForm


def index(request):
    return render_to_response('accounts/index.html', {}, {})


def admin_home(request):
    if request.user.is_authenticated():
        return render_to_response('accounts/homepage-admin.html')
    else:
        return HttpResponseRedirect('/')

def user_login(request):
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


def add_student(request):
    if request.user.is_authenticated():     
        form = AddStudentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save()
            return HttpResponse("weeeyy")
        else:
            context = {'add_student_form': form}
            return render(request, 'accounts/add_student.html', context)
    else:
        return HttpResponse("log in please")

