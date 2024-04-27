from django.urls import path

from .views import home_page_view, about_us_page_view, contact_us_page_view, faq_page_view, our_team_page_view, pricing_page_view, services_page_view, service_detail_page_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about_us/', about_us_page_view, name='about_us'),
    path('contact_us/', contact_us_page_view, name='contact_us'),
    path('faq/', faq_page_view, name='faq'),
    path('our_team/', our_team_page_view, name='our_team'),
    path('pricing/', pricing_page_view, name='pricing'),
    path('services/', services_page_view, name='services'),
    path('service_detail/<slug:slug>/', service_detail_page_view, name='service_detail'),
]