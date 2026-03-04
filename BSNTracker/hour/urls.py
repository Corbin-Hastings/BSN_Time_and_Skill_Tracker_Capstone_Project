from django.urls import path
from . import views

urlpatterns = [
    path("time_entry/",views.input_view,name="time entry"),
    path("hours/", views.hours, name = "hours"),
    path("passport/", views.passport, name = "passport"),
    path("share/", views.share , name="share")

]