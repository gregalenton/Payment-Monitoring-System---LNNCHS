from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):

    '''
    Homepage of Site
    '''
    template_name = 'homepage.html'

    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
            'page_title': 'Welcome To Vinna!',
        }
        if request.user and not request.user.is_anonymous():
            context = {
                'page_title': 'Welcome ' +
                str(request.user.get_full_name()),
            }
        return render(request, self.template_name, context)

    def login_user(request):
        state = "Please log in below..."
        username = password = ''
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = "You're successfully logged in!"
                else:
                    state = "Your account is not active, please contact the site admin."
            else:
                state = "Your username and/or password were incorrect."

        return render_to_response('auth.html',{'state':state, 'username': username})
