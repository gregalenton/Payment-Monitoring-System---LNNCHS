from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from accounts.models import Student
from funds.models import Due, Project
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import (reverse_lazy, reverse)

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view, login_url=reverse_lazy('accounts:Index'))

class AddFundsView(LoginRequiredMixin, generic.CreateView):
    template_name = 'funds/addfunds.html'
    form_class = forms.AddFundsForm

    def form_valid(self, form):
        # student = Student.objects.all()
        # cost = form.cleaned_data['cost']

        # if len(student)>0:
        #     for s in student:
        #         s.toPay = cost + s.toPay
        #         s.save()

        form.save(commit=True)
        return HttpResponseRedirect(reverse('accounts:Admin'))

    def form_invalid(self, form):
        # print form.firstname
        print "Invalid!"
        print form.errors
        return HttpResponseRedirect(reverse('funds:AddFunds'))

class EditFundsView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'funds/editfund.html'
    model = Due

    fields = ['fundname', 'cost']

    def get_success_url(self):
        return reverse('accounts:Admin')

    def get_context_data(self, **kwargs):
        context = super(EditFundsView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:EditFunds', kwargs={'pk': self.get_object().name})
        queryset = Student.objects.filter(pk=kwargs)
        # firstname = queryset[0].firstname
        print "Hello"
        return context

class ViewFundsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'funds/viewfund.html'

class ViewAllFundsView(LoginRequiredMixin, generic.ListView):
    template_name = 'funds/viewallfunds.html'

    def get_queryset(self):
        queryset = Due.objects.all()
        # print queryset
        return queryset


class AddProjectView(LoginRequiredMixin, generic.CreateView):
    template_name = 'funds/addproject.html'
    form_class = forms.AddProjectForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('accounts:Admin'))

    def form_invalid(self, form):
        # print form.firstname
        print "Invalid!"
        print form.errors
        return HttpResponseRedirect(reverse('funds:AddProject'))

class EditProjectsView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'funds/editproject.html'
    model = Project

    fields = ['name', 'receiver', 'cost']

    def get_success_url(self):
        return reverse('accounts:Admin')

    def get_context_data(self, **kwargs):
        context = super(EditProjectView, self).get_context_data(**kwargs)
        context['action'] = reverse('funds:editproject', kwargs={'pk': self.get_object().name})
        queryset = Project.objects.filter(pk=kwargs)
        # firstname = queryset[0].firstname
        print "Hello"
        return context

class ViewProjectsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'funds/viewproject.html'

class ViewAllProjectsView(LoginRequiredMixin, generic.ListView):
    template_name = 'funds/viewallproject.html'

    def get_queryset(self):
        queryset = Project.objects.all()
        # print queryset
        return queryset


class AddPaymentView(LoginRequiredMixin, generic.CreateView):
    template_name = 'funds/addpayment.html'
    form_class = forms.AddPaymentForm

    def form_valid(self, form):
        # student_id = form.cleaned_data['student_id']
        # payment = form.cleaned_data['cost']
        student = Student.objects.filter(student_id=student_id)

        toPay = student.toPay

        if toPay != 0:
            dif = toPay - payment
            student.toPay = dif
            paid = student.paid
            total = paid + payment
            student.paid = total
            student.save()
        else:
            return HttpResponseRedirect(reverse('accounts:ViewAllStudents'))
        return HttpResponseRedirect(reverse('accounts:ViewAllStudents'))

    def get_success_url(self):
        return reverse('accounts:Admin')

def get_payables(self):
        queryset = Due.objects.all()
        # print queryset
        return queryset