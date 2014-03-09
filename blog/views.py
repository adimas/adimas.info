from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from blog.models import Post

def blogs(request):
    posts = Post.objects.all().order_by('-created')[:5]
    paginator = Paginator(posts, 4)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts}
    return render(request, 'blogs.html', context)

def blog_post(request,post_id):
    post=Post.objects.filter(id=post_id);
    context = {'post': post}
    return render(request, 'blog_post.html', context)


  