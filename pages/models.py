from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
