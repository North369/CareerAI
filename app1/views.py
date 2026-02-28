from django.shortcuts import render

# Nút 1: Làm trắc nghiệm AI (Bot Phân tích/Tìm nghề)
def app1_view(request):
    return render(request, 'app1/app1.html')

# Nút 2: Đồng hành đạt ngành (Bot Holland mới)
def holland_view(request):
    return render(request, 'app1/holland_new.html') # Đổi tên file để tránh trùng lặp



from django.shortcuts import render

# Trang 1: Phân tích CV (Bot 1)
def app1_view(request):
    return render(request, 'app1/app1.html')

# Trang 2: Trắc nghiệm Holland (Bot 2)
def holland_view(request):
    return render(request, 'app1/holland.html')

# THÊM HÀM NÀY VÀO (Vì urls.py đang gọi nó)
def holland_menu(request):
    return render(request, 'app1/holland_menu.html')