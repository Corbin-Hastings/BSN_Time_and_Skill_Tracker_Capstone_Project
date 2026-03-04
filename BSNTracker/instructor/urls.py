from django.urls import path
from . import views

urlpatterns = [
    path("approval/",views.hour_approval,name="Approval"),

]