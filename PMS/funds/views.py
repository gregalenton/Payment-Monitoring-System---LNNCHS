from django.shortcuts import render, render_to_response
from django.views import generic
from . import forms
from . import models
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


class ViewFundsView(LoginRequiredMixin, generic.DetailView):
    model = models.Project
    template_name = 'funds/fundinfo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ViewFundsView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:viewfunds',
                                    kwargs={'pk': self.get_object().project_id})

        return context


class SearchFundsView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('funds/search_fund.html') 

    def FundInfoView(request):
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            fund = models.Project.objects.get(project_name=inp)
            return render(request, 'funds/search_fundinfo_result.html',
                {'student': student, 'query': inp})
        else:
            return HttpResponseRedirect('/funds/displayfundsearchresults/')  

class EditFundsView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    template_name = 'funds/edit_fund.html'
    fields = ['project_name', 'project_receiver', 'project_cost']

    def get_success_url(self):
        return reverse('funds:changessaved')

    def get_context_data(self, **kwargs):

        context = super(EditStudentView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:editfunds',
                                    kwargs={'pk': self.get_object().student_id})

        return context


    
class ChangesSaved(LoginRequiredMixin, generic.View):
    def get(self, request):
        return render_to_response('funds/changessaved.html')




def DisplayFundSearchResults(request):
    if 'input' in request.GET and request.GET['input']:
        inp = request.GET['input']
        funds = models.Project.objects.filter(project_name=inp)
        return render(request, 'funds/search_fund_result.html',
            {'funds': funds, 'query': inp})
    else:
        return HttpResponseRedirect('/funds/searchfunds/')