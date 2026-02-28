from django.shortcuts import render

def get_home(request):
    return render(request, 'home/home.html')

def register_view(request):
    # Tạm thời trả về một dòng chữ để kiểm tra link đã chạy chưa
    from django.http import HttpResponse
    return HttpResponse("Đây là trang Đăng ký thành viên")


from django.shortcuts import render

# Hàm cho trang chủ (đã có sẵn của bạn)
def get_home(request):
    return render(request, 'home/home.html')

# THÊM HÀM NÀY: Hàm xử lý cho trang app1
def app1_view(request):
    # Bạn có thể tạo file app1.html hoặc dùng tạm một file html có sẵn
    return render(request, 'home/app1.html') 

# THÊM HÀM NÀY: Hàm xử lý cho trang đăng ký
def register_view(request):
    return render(request, 'home/register.html')



from django.shortcuts import render

# Hàm cho trang chủ CareerAI (đã có sẵn)
def get_home(request):
    return render(request, 'home/home.html')

# THÊM HÀM NÀY: Xử lý trang App1
def app1_view(request):
    return render(request, 'home/app1.html')

# THÊM HÀM NÀY: Xử lý trang Đăng ký
def register_view(request):
    return render(request, 'home/register.html')