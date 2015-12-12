from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
        url(r'^$', views.HomeView.as_view(), name='home'),
        url(r'^accounts/login/$', views.user_login, name='login'),
        url(r'^accounts/home/$', views.AdminHomeView.as_view(), name='adminhome'),
        url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
        url(r'^accounts/addstudent/$', views.AddStudentView.as_view(), name='addstudent'),
        url(r'^accounts/editstudent/(?P<pk>\d+)/$', views.EditStudentView.as_view(), name='editstudent'),
        url(r'^accounts/searchstudent/$', views.SearchStudentView.as_view(), name='searchstudent'),
        url(r'^accounts/viewstudentinfo/(?P<pk>\d+)/$', views.ViewStudentInfoView.as_view(), name='viewstudentinfo'),
        url(r'^accounts/viewallstudents/$', views.ViewAllStudentsView.as_view(), name='viewallstudents'),
        url(r'^accounts/studentswithliabilities/$', views.StudentsWithLiabilitiesView.as_view(), name='studentswithliabilities'),
        url(r'^accounts/createpayment/$', views.CreatePaymentView.as_view(), name='createpayment'),
        url(r'^accounts/enterdiscount/$', views.EnterDiscountView.as_view(), name='enterdiscount'),
        #url(r'^accounts/displaysearchresults/$', views.DisplaySearchResults.as_view(), name='displaysearchresults'),
        url(r'^accounts/displaysearchresults/$', views.DisplaySearchResults, name='displaysearchresults'),  
        url(r'^accounts/displayresults/$', views.DisplayResults, name='displayresults'),  
        )
