from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    cover = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    author_avatar = models.ImageField(upload_to='author_avatar/')
    author_information = models.TextField()
    author_social_link = models.URLField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    datetime_created = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.post.id])
    
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    


    