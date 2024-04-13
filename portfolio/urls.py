from django.urls import path

from .views import portfolio_page_view, portfolio_detail_page_view

urlpatterns = [
    path('', portfolio_page_view, name='portfolio'),
    path('detail/', portfolio_detail_page_view, name='portfolio_detail')
]
