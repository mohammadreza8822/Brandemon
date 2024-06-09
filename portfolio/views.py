from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from requests import Request

from .models import Portfolio, Category


class PortfolioListView(generic.ListView):
    model = Portfolio
    queryset = Portfolio.objects.select_related('category').all()
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'portfolios'
        

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'
    
    
class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.prefetch_related('portfolios').all()
    