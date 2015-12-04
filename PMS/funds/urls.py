from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^Funds', views.FundsView.as_view(), name="Funds"),
]