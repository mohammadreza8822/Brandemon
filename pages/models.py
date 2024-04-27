from django.db import models


class Services(models.Model):
    WEB = 'flaticon-web-development'
    WEB_2 = 'flaticon-web-domain'
    TECHNOLOGY = 'flaticon-nanotechnology'
    DEVELOPE = 'flaticon-profile'
    SEO = 'flaticon-search'
    ICONS_CHOICES = ((WEB, WEB),
                     (WEB_2, WEB_2),
                     (TECHNOLOGY, TECHNOLOGY),
                     (DEVELOPE, DEVELOPE),
                     (SEO, SEO),
                     )
    icon = models.CharField(max_length=255, choices=ICONS_CHOICES)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    title_info = models.CharField(max_length=255)
    number_info = models.IntegerField(max_length=2)
    text_info = models.TextField()
