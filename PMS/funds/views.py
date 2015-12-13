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
        student = StudentInfo.objects.all()
        due_cost = form.cleaned_data['due_cost']

        if len(student) > 0:
            for s in student:
                s.student_toPay = due_cost+s.student_toPay
                s.save()

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

    def form_valid(self, form):
        due_id = self.get_object().due_id
        due = models.Due.objects.get(due_id=due_id)
        current_value = due.due_cost
        new_value = form.cleaned_data['due_cost']
        fund = form.save(commit=False)
        students = StudentInfo.objects.all()

        if len(students) > 0:
            for s in students:
                s.student_toPay = s.student_toPay - current_value
                s.student_toPay = s.student_toPay + new_value
                s.save()
        return super(EditFundsView, self).form_valid(form)

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
        projects = models.Project.objects.all()
        total1 = 0

        for p in projects:
            total1 = p.project_cost+total1

        total = 0

        for s in students:
            total = s.student_paid+total

        total = total-total1

        context['total'] = total

        return context


class AddProjectView(LoginRequiredMixin, generic.CreateView):
    template_name = 'funds/add_project.html'
    form_class = forms.AddProjectForm

    def form_valid(self, form):
        return super(AddProjectView, self).form_valid(form)

    def get_success_url(self):
        return reverse('funds:changessaved')


class SearchProjectView(LoginRequiredMixin, generic.View):
    def get(self, request):
            return render_to_response('funds/search_project.html') 

    def ProjectInfoView(request):
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            project = models.Project.objects.get(project_name=inp)
            return render(request, 'funds/search_projectinfo_result.html',
                {'project': project, 'query': inp})
        else:
            return HttpResponseRedirect('/funds/displayprojectsearchresults/')  


class EditProjectView(LoginRequiredMixin, generic.UpdateView):
    model = models.Project
    template_name = 'funds/edit_project.html'
    fields = ['project_name', 'project_receiver', 'project_cost']

    def get_success_url(self):
        return reverse('funds:changessaved')

    def get_context_data(self, **kwargs):

        context = super(EditProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:editproject',
                                    kwargs={'pk': self.get_object().project_id})

        return context


class ViewProjectView(LoginRequiredMixin, generic.DetailView):
    model = models.Project
    template_name = 'funds/projectinfo_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super(ViewProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:viewproject',
                                    kwargs={'pk': self.get_object().project_id})

        return context


class ViewAllProjectsView(LoginRequiredMixin, generic.ListView):
    model = models.Project
    template_name = 'funds/viewallprojects.html'

    def get_context_data(self, **kwargs):

        context = super(ViewAllProjectsView, self).get_context_data(**kwargs)        
        projects = models.Project.objects.all()

        total = 0

        for p in projects:
            total = p.project_cost+total

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


def DisplayProjectSearchResults(request):
    if request.user.is_authenticated():
        if 'input' in request.GET and request.GET['input']:
            inp = request.GET['input']
            projects = models.Project.objects.filter(project_name=inp)
            return render(request, 'funds/search_project_result.html',
                {'projects': projects, 'query': inp})
        else:
            return HttpResponseRedirect('/funds/searchproject/')
    else:
        return HttpResponseRedirect('/accounts/login')