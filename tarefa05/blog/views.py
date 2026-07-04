from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {"posts": posts,}
    return render(request, 'blog/index.html', context)    

def post(request, id_post):
    post = get_object_or_404(Post, id=id_post)
    context={"post" : post,}
    return render(request, 'blog/post.html', context)    