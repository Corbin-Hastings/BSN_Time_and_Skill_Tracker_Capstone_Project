from django.urls import path
from . import views

urlpatterns = [
    path("time_entry/",views.input_view,name="time entry"),



]