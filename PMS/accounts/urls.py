from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^accounts/login/$', views.user_login, name='login'),
        url(r'^accounts/home/$', views.admin_home, name='home'),
        url(r'^accounts/logout/$', views.user_logout, name='logout'),
        url(r'^accounts/addstudent/$',views.add_student, name='addstudent'),
        )