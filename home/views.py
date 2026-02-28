from django.shortcuts import render

from django.http import HttpResponse

# 1. Trang chủ: gọi file home.html trong thư mục home
def get_home(request):
    return render(request, 'home/home.html')

# 2. Trang App1: gọi file app1.html trong thư mục app1
def app1_view(request):
    return render(request, 'app1/app1.html')

# 3. Trang Đăng ký: Vì bạn chưa có file register.html nên dùng tạm HttpResponse để tránh lỗi
def register_view(request):
    return HttpResponse("Đây là trang Đăng ký thành viên - Hệ thống đang cập nhật giao diện.")




from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')