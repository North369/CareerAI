from django.urls import path
from . import views

urlpatterns = [
    # Đường dẫn này sẽ khớp với trang chủ (chuỗi trống)
    path('', views.get_home, name='home'), 
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('register/', views.register_view, name='dang_ky'), # Thêm dòng này


    path('register/', views.register_view, name='register'), # Đường dẫn cho trang đăng ký, tham số name
path('app1/', views.app1_view, name='app1_home'), 
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'), # Trang chủ
    path('app1/', views.app1_view, name='app1_home'), # Khớp với name bạn dùng ở thẻ <a>
    path('register/', views.register_view, name='register'), # Khớp với name bạn dùng ở thẻ <a>
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('app1/', views.app1_view, name='app1_home'), # Đã thêm tham số name
    path('register/', views.register_view, name='register'), # Đã thêm tham số name
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    # Đừng khai báo app1 ở đây nếu bạn đã khai báo trong site1/urls.py
]








from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view),
]