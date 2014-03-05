from django import template
from filebrowser.base import FileObject
from blog.models import Post

register = template.Library()
@register.simple_tag
def get_teaser_image(path, version):
    if path:
        image = FileObject(path)
        if image.filetype == "Image":
            return  image.version_generate(version).url.split('adimas.info')[1]
    else:
        return ""
