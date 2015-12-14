from django.conf.urls import include, url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^funds', views.AddFundsView.as_view(), name="AddFunds"),
    url(r'^edit_funds', views.EditFundsView.as_view(), name="EditFunds"),
    url(r'^view_funds', views.ViewFundsView.as_view(), name="ViewFunds"),
    url(r'^view_all_funds', views.ViewAllFundsView.as_view(), name="ViewAllFunds"),
    url(r'^project', views.AddProjectView.as_view(), name="AddProject"),
    url(r'^edit_project', views.EditProjectsView.as_view(), name="EditProjects"),
    url(r'^view_project', views.ViewProjectsView.as_view(), name="ViewProjects"),
    url(r'^view_all_projects', views.ViewAllProjectsView.as_view(), name="ViewAllProjects"),
    url(r'^add_payment', views.AddPaymentView.as_view(), name="AddPayment"),
)