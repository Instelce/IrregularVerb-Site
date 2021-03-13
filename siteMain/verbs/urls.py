from django.urls import path
from . import views

urlpatterns = [
    path('', views.verb_list, name="home"),
]
