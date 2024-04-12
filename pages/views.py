from django.shortcuts import render


def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_page_view(request):
    return render(request, 'pages/about_us.html')

def contact_us_page_view(request):
    return render(request, 'pages/contact_us.html')

def faq_page_view(request):
    return render(request, 'pages/faq.html')

def our_team_page_view(request):
    return render(request, 'pages/our_team.html')

def pricing_page_view(request):
    return render(request, 'pages/pricing.html')

def services_page_view(request):
    return render(request, 'pages/services.html')

def service_detail_page_view(request):
    return render(request, 'pages/service_detail.html')