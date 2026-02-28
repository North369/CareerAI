from django.shortcuts import render


def app1_view(request):
    return render(request, 'app1/app1.html')


def holland_view(request):
    return render(request, 'app1/holland_new.html') 



from django.shortcuts import render


def app1_view(request):
    return render(request, 'app1/app1.html')


def holland_view(request):
    return render(request, 'app1/holland.html')


def holland_menu(request):
    return render(request, 'app1/holland_menu.html')