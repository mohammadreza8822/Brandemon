from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('<slug:slug>/', views.PortfolioDetailView.as_view(), name='portfolio_detail')
]
