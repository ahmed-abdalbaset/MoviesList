from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path("about/", views.welcome_page, name = 'welcome_page'),
               path('movies/' ,views.Movies_list, name ='Movies_list'),
               path('' ,views.home_page , name ='home page'),
               ]