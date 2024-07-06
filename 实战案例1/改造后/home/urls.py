from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("salescheck", views.salescheck, name="salescheck"),
    path("addsalescheck", views.addsalescheck, name="addsalescheck"),
]
