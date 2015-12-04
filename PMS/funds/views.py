from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class FundsView(generic.TemplateView):
    template_name = 'funds/funds.html'



