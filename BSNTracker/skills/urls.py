from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('view-skills/', views.skills_list, name="list"),
    path('log-skills/', views.log_new, name="log-skills"),
    path("passport/", views.passport, name = "passport"),
    path("share/<int:user>/<uuid:token>/", views.share , name="share")
]