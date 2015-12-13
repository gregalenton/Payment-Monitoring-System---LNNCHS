from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^funds', views.AddFundsView.as_view(), name="add_funds"),
]