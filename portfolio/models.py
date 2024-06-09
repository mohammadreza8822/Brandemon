from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title

class Portfolio(models.Model):
    cover = models.ImageField(upload_to='portfolio/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    customer = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios')
    datetime_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('portfolio_detail', kwargs={"slug": self.slug})