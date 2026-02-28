from django.shortcuts import render

# Trang Phân tích CV
def app1_view(request):
    return render(request, 'app1/app1.html')

# Trang Trắc nghiệm Holland
def holland_view(request):
    return render(request, 'app1/holland.html')

# Các trang menu bổ trợ (nếu cần)
def holland_menu(request):
    return render(request, 'app1/holland_menu.html')