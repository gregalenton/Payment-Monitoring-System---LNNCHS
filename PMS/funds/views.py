from django.shortcuts import render, render_to_response
from django.views import generic
from . import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import (reverse_lazy, reverse)
# Create your views here.

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:login'))
        

class AddFundsView(LoginRequiredMixin, generic.CreateView):
    template_name = 'funds/add_fund.html'
    form_class = forms.AddFundsForm

    def form_valid(self, form):
        return super(AddFundsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('funds:changessaved')

class ViewFundsView(LoginRequiredMixin, generic.View):
    pass


class SearchFundsView(LoginRequiredMixin, generic.View):
    pass

class EditFundsView(LoginRequiredMixin, generic.View):
    pass
    
class ChangesSaved(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('funds/changessaved.html')