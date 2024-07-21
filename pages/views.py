from django.shortcuts import render, get_object_or_404

from portfolio.models import Portfolio, Category
from blog.models import Comment
from blog.models import Post
from .forms import ContactUsForm
from .models import ContactUs, OurTeam, Faq, Price

def home_page_view(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    price = Price.objects.all()
    post = Post.objects.all()
    comment = Comment.objects.order_by('-datetime_created').all()
    if category_id:
        portfolio_items = Portfolio.objects.filter(category_id=category_id)
    else:
        portfolio_items = Portfolio.objects.all()
    return render(request, 'pages/home.html', context={'prices': price,
                                                       'posts': post,
                                                        'comments': comment,
                                                        'categories': categories,
                                                        'portfolio_items': portfolio_items,
                                                        'selected_category': category_id})

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
    faq = Faq.objects.all()
    return render(request, 'pages/faq.html', context={'faq': faq})

def our_team_page_view(request):
    team = OurTeam.objects.all()
    return render(request, 'pages/our_team.html', context={'ourteam': team})

def pricing_page_view(request):
    price = Price.objects.all()
    return render(request, 'pages/pricing.html', context={'prices': price})

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

        