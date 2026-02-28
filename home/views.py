from django.shortcuts import render

from django.http import HttpResponse


def get_home(request):
    return render(request, 'home/home.html')


def app1_view(request):
    return render(request, 'app1/app1.html')


def register_view(request):
    return HttpResponse("Đây là trang Đăng ký thành viên - Hệ thống đang cập nhật giao diện.")




from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')