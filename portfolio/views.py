from django.shortcuts import render


def portfolio_page_view(request):
    return render(request, 'portfolio/portfolio.html')


def portfolio_detail_page_view(request):
    return render(request, 'portfolio/portfolio_detail.html')