from django.shortcuts import render

from blog.models import Post

def blogs(request):
    latest_blog_list = Post.objects.all().order_by('-created')[:5]
    context = {'latest_blog_list': latest_blog_list}
    return render(request, 'blogs.html', context)

def blog_post(request,post_id):
    current_blog_post=Post.objects.filter(id=post_id);
    context = {'current_blog_post': current_blog_post}
    return render(request, 'blog_post.html', context)