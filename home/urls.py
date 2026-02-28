from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.get_home, name='home'), 
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('register/', views.register_view, name='dang_ky'), 


    path('register/', views.register_view, name='register'),
path('app1/', views.app1_view, name='app1_home'), 
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('app1/', views.app1_view, name='app1_home'), 
    path('register/', views.register_view, name='register'), 
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('app1/', views.app1_view, name='app1_home'), 
    path('register/', views.register_view, name='register'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    
]








from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view),
]