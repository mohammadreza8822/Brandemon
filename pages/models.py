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