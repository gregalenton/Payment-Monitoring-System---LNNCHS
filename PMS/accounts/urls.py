from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
        url(r'^$', views.HomeView.as_view(), name='home'),
        url(r'^accounts/login/$', views.user_login, name='login'),
        url(r'^accounts/home/$', views.AdminHomeView.as_view(), name='adminhome'),
        url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
        url(r'^accounts/addstudent/$', views.AddStudentView.as_view(), name='addstudent'),
        url(r'^accounts/editstudent/$', views.EditStudentView, name='editstudent'),
        #url(r'^accounts/editstudent/$', views.EditStudentView.as_view(), name='editstudent'),
        url(r'^accounts/searchstudent/$', views.SearchStudentView.as_view(), name='searchstudent'),
        #url(r'^accounts/displaysearchresults/$', views.DisplaySearchResults.as_view(), name='displaysearchresults'),
        url(r'^accounts/displaysearchresults/$', views.DisplaySearchResults, name='displaysearchresults'),  
        )