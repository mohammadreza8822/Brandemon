from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Services
from .serializer import ContactUsSerializer


def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_page_view(request):
    return render(request, 'pages/about_us.html')

@api_view(['POST'])
def contact_us_page_view(request):
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return render(request, 'pages/contact_us.html')

def faq_page_view(request):
    return render(request, 'pages/faq.html')

def our_team_page_view(request):
    return render(request, 'pages/our_team.html')

def pricing_page_view(request):
    return render(request, 'pages/pricing.html')

def services_page_view(request):
    return render(request, 'pages/services.html')

        