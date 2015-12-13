from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^funds', views.AddFundsView.as_view(), name="AddFunds"),
    url(r'^project', views.AddProjectView.as_view(), name="AddProject"),
    url(r'^view_all_funds', views.ViewAllFundsView.as_view(), name="ViewAllFunds"),
    url(r'^view_all_projects', views.ViewAllProjectsView.as_view(), name="ViewAllProjects"),
    url(r'^add_payment', views.AddPaymentView.as_view(), name="AddPayment"),

]