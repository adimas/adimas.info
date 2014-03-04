from django.db import models
from django.contrib.auth.models import User
#from tinymce import models as tinymce_models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    teaser_image = models.ImageField(upload_to='static/uploads', max_length=100,blank=True)
    teaser_content = models.TextField(max_length=500)
    content = models.TextField()
    created = models.DateTimeField()
    source_url = models.URLField(blank=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    
