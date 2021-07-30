from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="home"),
    path('activities/<slug:slug>', views.activities, name="activities")

]