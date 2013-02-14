# Create your views here.
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse, render_to_response
from myapp.models import BlogPost
def blogIndex(request):
    blogPosts= BlogPost.objects.all()
    return render_to_response("blog_index.html", {"blogPosts":blogPosts})


def blogPost(request, postID):
    blogPost= BlogPost.objects.get(id=postID)
    return render_to_response("blog_post.html", {"blogPost":blogPost})


