from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import forms


class FundsView(generic.TemplateView):
    template_name = 'funds/funds.html'


class AddFundsView(generic.CreateView):
    template_name = 'funds/addfunds.html'
    form_class = forms.AddFundsForm

    def form_valid(self, form):
        return super(AddFundsView, self).form_valid(form)

    def get_success_url(self):
        return reverse('accounts:Admin')



