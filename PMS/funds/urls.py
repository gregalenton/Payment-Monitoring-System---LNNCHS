from django.conf.urls import patterns, url
from funds import views


urlpatterns = patterns('',
        url(r'^funds/addfunds/$', views.AddFundsView.as_view(), name='addfunds'),
        url(r'^funds/editfunds/(?P<pk>\d+)/$', views.EditFundsView.as_view(), name='editfunds'),
        url(r'^funds/viewfunds/(?P<pk>\d+)/$', views.ViewFundsView.as_view(), name='viewfunds'),
        url(r'^funds/searchfunds/$', views.SearchFundsView.as_view(), name='searchfunds'),
        url(r'^funds/changessaved/$', views.ChangesSaved.as_view(), name='changessaved'),
        url(r'^funds/displayfundsearchresults/$', views.DisplayFundSearchResults, name='displayfundsearchresults'),  
       
        # url(r'^accounts/home/$', views.AdminHomeView.as_view(), name='adminhome'),
        )