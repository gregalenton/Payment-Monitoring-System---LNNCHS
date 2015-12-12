from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name="Index"),
    url(r'^Admin_Login', views.AdminLoginView.as_view(), name="AdminLogin"),
    url(r'^Student_login',views.StudentLoginView.as_view(), name="StudentLogin"),
    url(r'^Admin', views.AdminView.as_view(), name="Admin"),
    url(r'^Students', views.AdminStudents.as_view(), name="Students"),
    url(r'^Add_Student', views.AddStudentView.as_view(), name="AddStudent"),
    url('',include('django.contrib.auth.urls',namespace='auth')),
)