from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms
from accounts.models import Student


class FundsView(generic.TemplateView):
    template_name = 'funds/funds.html'


class AddFundsView(generic.CreateView):
    template_name = 'funds/addfunds.html'
    form_class = forms.AddFundsForm

    def form_valid(self, form):
        student = Student.objects.all()
        cost = form.cleaned_data['cost']

        if len(student)>0:
            for s in student:
                s.student_toPay = cost + s.student_toPay
                s.save()

        form.save(commit=True)
        return HttpResponseRedirect(reverse('accounts:Admin'))

    def form_invalid(self, form):
        # print form.firstname
        print "Invalid!"
        print form.errors
        return HttpResponseRedirect(reverse('funds:AddFunds'))

class AddProjectView(generic.CreateView):
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


class ViewAllFundsView(generic.ListView):
    template_name = 'funds/viewallfunds.html'


class ViewAllProjectsView(generic.ListView):
    template_name = 'funds/viewallproject.html'


class AddPaymentView(generic.CreateView):
    template_name = 'funds/addpayment.html'
    form_class = forms.AddPaymentForm

    def form_valid(self, form):
        return super(AddPaymentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:Admin')