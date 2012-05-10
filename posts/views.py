from django.template import RequestContext, loader
from django.http import HttpResponse
from posts.models import Post, PostImage
from django.shortcuts import render_to_response, get_object_or_404

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def index(request, page_name):
    posts_list = Post.objects.filter(pageName='').order_by('-created')
    t = loader.get_template('posts/index.html')
    c = RequestContext(request, {
        'page_name': page_name, 
        'posts_list': posts_list
    })
    return HttpResponse(t.render(c))

def selected(request, page_name):
    post = get_object_or_404(Post, pageName=page_name)
    image = get_or_none(PostImage, post=post.id)
    t = loader.get_template('posts/selected.html')
    c = RequestContext(request, {
        'post': post,
        'image': image,
        'page_name': page_name
    })
    return HttpResponse(t.render(c))

