from django.shortcuts import render
from .models import Post

# Create your views here.
def post(request):
    posts=Post.objects.all().values()
    return render(
        request,
        'blog/post/post.html',
        {
            'posts':posts,
        })
    
def post_detail(request,slug):
    poss_de=Post.objects.filter(slug__iexact=slug)
    return render(request,
                  'blog/post/post_detail.html',
                  {'post':poss_de})