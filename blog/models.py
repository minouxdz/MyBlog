from django.db import models
from django.conf import settings
class Post(models.Model):
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Options(models.TextChoices):
        PUBLISHED='PUBLISHED'
        DRAFT='DRAFT'
    status=models.CharField(choices=Options,max_length=255,default=Options.DRAFT)