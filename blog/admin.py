from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from blog.models import Post
from mce_filebrowser.admin import MCEFilebrowserAdmin

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

# we define our resources to add to admin pages
class CommonMedia:
    js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/dojo/editor.js',
    )
    css = {
    'all': ('/static/dojo/editor.css',),
    }

#admin.site.register(Post)
# Example how to add rich editor capabilities to your models in admin.

# let's add it to this model
admin.site.register(Post,Media = CommonMedia)
