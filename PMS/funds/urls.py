from django.conf.urls import patterns, url
from funds import views


urlpatterns = patterns('',
        url(r'^funds/addfunds/$', views.AddFundsView.as_view(), name='addfunds'),
        url(r'^funds/editfunds/(?P<pk>\d+)/$', views.EditFundsView.as_view(), name='editfunds'),
        url(r'^funds/viewfunds/(?P<pk>\d+)/$', views.ViewFundsView.as_view(), name='viewfunds'),
        url(r'^funds/viewallfunds/$', views.ViewAllFundsView.as_view(), name='viewallfunds'),
        url(r'^funds/searchfunds/$', views.SearchFundsView.as_view(), name='searchfunds'),
        url(r'^funds/viewmoneyonhand/$', views.ViewMoneyOnHandView.as_view(), name='viewmoneyonhand'),
        url(r'^funds/addproject/$', views.AddProjectView.as_view(), name='addproject'),
        url(r'^funds/searchproject/$', views.SearchProjectView.as_view(), name='searchproject'),    
        url(r'^funds/editproject/(?P<pk>\d+)/$', views.EditProjectView.as_view(), name='editproject'),
        url(r'^funds/viewproject/(?P<pk>\d+)/$', views.ViewProjectView.as_view(), name='viewproject'),
        url(r'^funds/viewallprojects/$', views.ViewAllProjectsView.as_view(), name='viewallprojects'),     
        url(r'^funds/changessaved/$', views.ChangesSaved.as_view(), name='changessaved'),
        url(r'^funds/displayfundsearchresults/$', views.DisplayFundSearchResults, name='displayfundsearchresults'),       
        url(r'^funds/displayprojectsearchresults/$', views.DisplayProjectSearchResults, name='displayprojectsearchresults'),       
        # url(r'^accounts/home/$', views.AdminHomeView.as_view(), name='adminhome'),
        )