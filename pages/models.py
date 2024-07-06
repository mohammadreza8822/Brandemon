from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()


class OurTeam(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Team/')
    facebook_social_media_link = models.URLField(max_length=255, null=True, blank=True)
    youtube_social_media_link = models.URLField(max_length=255, null=True, blank=True)
    instagram_social_media_link = models.URLField(max_length=255, null=True, blank=True)
    twiter_social_media_link = models.URLField(max_length=255, null=True, blank=True)


class Faq(models.Model):
    title = models.CharField(max_length=500)
    text = models.TextField()


class Price(models.Model):
    POPULAR = 'popular'
    UNPOPULAR = 'unpopular'
    p_choices = [
        (POPULAR, 'popular'),
        (UNPOPULAR, 'unpopular')
    ]
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(max_length=20)
    description = models.TextField()
    popular_field = models.CharField(max_length=100, choices=p_choices)