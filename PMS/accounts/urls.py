from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name="Index"),
                       url(r'^admin_login', views.AdminLoginView.as_view(), name="AdminLogin"),
                       url(r'^student_login',views.StudentLoginView.as_view(), name="StudentLogin"),
                       url(r'^Admin', views.AdminView.as_view(), name="Admin"),
                       url(r'^student', views.StudentView.as_view(), name="Student"),
                       url(r'^add_student', views.AddStudentView.as_view(), name="AddStudent"),
                       url(r'^edit_student', views.EditStudentView.as_view(), name="EditStudent"),
                       url(r'^view_student', views.ViewStudentView.as_view(), name="ViewStudent"),
                       url(r'^view_all_students', views.ViewAllStudents.as_view(), name="ViewAllStudents"),
                       url('',include('django.contrib.auth.urls',namespace='auth')),
                       )