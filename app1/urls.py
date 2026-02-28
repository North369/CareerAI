from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1_view, name='app1_home'),
    path('holland-test/', views.holland_view, name='holland_test'),
    path('menu/', views.holland_menu, name='holland_menu'),
]