from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
from requests import Request

from .models import Portfolio, Category


def portfolio_list(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        # category = get_object_or_404(Category, id=category_id)
        portfolio_items = Portfolio.objects.filter(category_id=category_id)

    else:
        portfolio_items = Portfolio.objects.all()

    return render(request, 'portfolio/portfolio_list.html', {
        'categories': categories,
        'portfolio_items': portfolio_items,
        'selected_category': category_id,
    })
        

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
    context_object_name = 'portfolio'
    
    
class CategoryListView(generic.ListView):
    model = Category
    queryset = Category.objects.prefetch_related('portfolios').all()
    