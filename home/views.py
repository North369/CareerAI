from django.shortcuts import render

# Trang chủ nằm trong app home
def get_home(request):
    return render(request, 'home/home.html')

# Trang app1 nằm trong thư mục templates của app1
def app1_view(request):
    return render(request, 'app1/app1.html') 

# Trang đăng ký (Nếu bạn chưa tạo register.html thì dùng tạm home.html để không bị lỗi 500)
def register_view(request):
    # Nếu bạn đã có file register.html trong home/templates/home/ thì để nguyên
    # Nếu chưa có, hãy đổi thành 'home/home.html' để test link
    return render(request, 'home/home.html')