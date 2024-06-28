from django.shortcuts import render, get_object_or_404

from .forms import ContactUsForm
from .models import ContactUs

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_page_view(request):
    return render(request, 'pages/about_us.html')

def contact_us_page_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.contact_us = ContactUs()
            new_comment.save()
            form = ContactUsForm()
    else:
        form = ContactUsForm()
    return render(request, 'pages/contact_us.html', context={'contact_us_form': form})

def faq_page_view(request):
    return render(request, 'pages/faq.html')

def our_team_page_view(request):
    return render(request, 'pages/our_team.html')

def pricing_page_view(request):
    return render(request, 'pages/pricing.html')

def services_page_view(request):
    return render(request, 'pages/services.html')

def service_web_view(request):
    return render(request, 'pages/service_web.html')

def service_instagram_view(request):
    return render(request, 'pages/service_instagram.html')

def service_video_view(request):
    return render(request, 'pages/service_video.html')

def service_ads_view(request):
    return render(request, 'pages/service_ads.html')

        