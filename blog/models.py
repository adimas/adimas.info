from django.db import models
from django.contrib.auth.models import User
#from tinymce import models as tinymce_models
from taggit.managers import TaggableManager
from filebrowser.base import FileObject


class Post(models.Model):
    title = models.CharField(max_length=100)
    teaser_image = models.ImageField(u"Teaser image", max_length=250, upload_to='static/img/uploads', blank=True, null=True)
    teaser_content = models.TextField(max_length=500)
    content = models.TextField()
    created = models.DateTimeField()
    source_url = models.URLField(blank=True)
    tags = TaggableManager(blank=True)
    author = models.ForeignKey(User)

    def teaser_image_object(self):
        if self.teaser_image:
            return FileObject(self.teaser_image.path)
        return None   
    teaser_image_object.allow_tags = True
    def __unicode__(self):
        return self.title
    
