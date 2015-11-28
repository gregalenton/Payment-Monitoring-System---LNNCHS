from django.conf.urls import patterns, url
from funds import views


urlpatterns = patterns('',
        url(r'^accounts/addfunds/$', views.AddFundsView.as_view(), name='addfunds'),
        url(r'^accounts/editfunds/$', views.EditFundsView.as_view(), name='editfunds'),
        url(r'^accounts/viewfunds/$', views.ViewFundsView.as_view(), name='viewfunds'),
        url(r'^accounts/searchfunds/$', views.SearchFundsView.as_view(), name='searchfunds'),
        url(r'^accounts/changessaved/$', views.ChangesSaved.as_view(), name='changessaved'),
        # url(r'^accounts/login/$', views.user_login, name='login'),
        # url(r'^accounts/home/$', views.AdminHomeView.as_view(), name='adminhome'),
        )