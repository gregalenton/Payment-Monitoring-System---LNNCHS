from django.shortcuts import render, render_to_response
from django.views import generic
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import (reverse_lazy, reverse)
from django.http import HttpResponseRedirect, HttpResponse
from accounts.models import StudentInfo
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


class ViewFundsView(LoginRequiredMixin, generic.DetailView):
    model = models.Due
    template_name = 'funds/fundinfo_detail.html'
    context_object_name = 'fund'

    def get_context_data(self, **kwargs):
        context = super(ViewFundsView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:viewfunds',
                                    kwargs={'pk': self.get_object().due_id})

        return context


class SearchFundsView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('funds/search_fund.html') 

    def FundInfoView(request):
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            fund = models.Due.objects.get(due_name=inp)
            return render(request, 'funds/search_fundinfo_result.html',
                {'fund': fund, 'query': inp})
        else:
            return HttpResponseRedirect('/funds/displayfundsearchresults/')  


class EditFundsView(LoginRequiredMixin, generic.UpdateView):
    model = models.Due
    template_name = 'funds/edit_fund.html'
    fields = ['due_name', 'due_cost']

    def get_success_url(self):
        return reverse('funds:changessaved')

    def get_context_data(self, **kwargs):

        context = super(EditFundsView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:editfunds',
                                    kwargs={'pk': self.get_object().due_id})

        return context


class ViewAllFundsView(LoginRequiredMixin, generic.ListView):
    model = models.Due
    template_name = 'funds/viewallfunds.html'

    def get_context_data(self, **kwargs):

        context = super(ViewAllFundsView, self).get_context_data(**kwargs)        
        projects = models.Due.objects.all()

        total = 0

        for p in projects:
            total = p.due_cost+total

        context['total'] = total

        return context


class ViewMoneyOnHandView(LoginRequiredMixin, generic.ListView):
    model = StudentInfo
    template_name = 'funds/view_money_onhand.html'

    def get_context_data(self, **kwargs):

        context = super(ViewMoneyOnHandView, self).get_context_data(**kwargs)        
        students = StudentInfo.objects.all()

        total = 0

        for s in students:
            total = s.student_paid+total

        context['total'] = total

        return context



class ChangesSaved(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('funds/changessaved.html')


def DisplayFundSearchResults(request):
    if request.user.is_authenticated():
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            funds = models.Due.objects.filter(due_name=inp)
            return render(request, 'funds/search_fund_result.html',
                {'funds': funds, 'query': inp})
        else:
            return HttpResponseRedirect('/funds/searchfunds/')
    else:
        return HttpResponseRedirect('/accounts/login')