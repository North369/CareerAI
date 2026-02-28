from django.urls import path
from . import views

urlpatterns = [
    # Truy cập: /app1/ -> Ra trang Phân tích CV
    path('', views.app1_view, name='app1_home'),
    
    # Truy cập: /app1/holland-test/ -> Ra trang Trắc nghiệm Holland
    path('holland-test/', views.holland_view, name='holland_test'),
    
    # Các path khác nếu bạn muốn dùng menu
    path('menu/', views.holland_menu, name='holland_menu'),
]