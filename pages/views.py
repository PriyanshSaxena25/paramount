from django.shortcuts import render

def landing_page(request):
    return render(request, 'pages/landing.html')

def inventory(request):
    return render(request, 'pages/inventory.html')

def demand_tracker(request):
    return render(request, 'pages/demand_tracker.html')

def cr_tracker(request):
    return render(request, 'pages/cr_tracker.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')