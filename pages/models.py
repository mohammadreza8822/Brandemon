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
    icon = models.ImageField(upload_to='foods/')
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='foods/', null=True, blank=True)
    title_info = models.CharField(max_length=255)
    number_info = models.IntegerField(max_length=2)
    text_info = models.TextField()


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
