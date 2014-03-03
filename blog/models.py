from django.db import models
from django import forms
from tinymce import models as tinymce_models
from taggit.managers import TaggableManager
from adimas import settings


# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=100)
    content= tinymce_models.HTMLField()
    created = models.DateTimeField()
    tags = TaggableManager()
    
    def __unicode__(self):
        return self.title
    
