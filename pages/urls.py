from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about_us/', views.about_us_page_view, name='about_us'),
    path('contact_us/', views.contact_us_page_view, name='contact_us'),
    path('faq/', views.faq_page_view, name='faq'),
    path('our_team/', views.our_team_page_view, name='our_team'),
    path('pricing/', views.pricing_page_view, name='pricing'),
    path('services/', views.services_page_view, name='services'),
    path('service_web/', views.service_web_view, name='service_web'),
    path('service_instagram/', views.service_instagram_view, name='service_instagram'),
    path('service_video/', views.service_video_view, name='service_video'),
    path('service_ads/', views.service_ads_view, name='service_ads'),
]