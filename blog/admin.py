from django.contrib import admin

# Register your models here.
from blog.models import Post
from mce_filebrowser.admin import MCEFilebrowserAdmin

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(Post)

