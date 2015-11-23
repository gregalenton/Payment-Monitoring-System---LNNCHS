from django.conf.urls import patterns, url, include
from accounts import views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
        url(r'^index/$', views.index, name='index'),
        url(r'^accounts/login/$', views.user_login, name='login'),
        url(r'^accounts/home/$', views.admin_home, name='home'),
        url(r'^accounts/logout/$', views.user_logout, name='logout'),
        url(r'^accounts/addstudent/$',views.add_student, name='addstudent'),
        ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)