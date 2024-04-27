from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Services
from .serializer import ServicesSerializer


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

@api_view()
def services_page_view(request):
    if request.method == 'GET':
        service_queryset = Services.objects.all()
        serializer = ServicesSerializer(service_queryset,)
        return Response(serializer.data)

def service_detail_page_view(request, slug):
    if request.method == 'GET':
        service_queryset = Services.objects.all()
        serializer = ServicesSerializer(service_queryset,)
        return Response(serializer.data)
        return render(request, 'pages/service_detail.html')