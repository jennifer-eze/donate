from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('startFund/', views.startFund, name='startFund'),
    path('donate/', views.donate, name='donate')
]