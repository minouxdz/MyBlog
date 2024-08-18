from django.shortcuts import render,get_object_or_404
from .models import Post
def PostList(request):

    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'list.html',context)

def PostDetails(request,id):
    post=get_object_or_404(Post,id=id)
    context={'post':post}
    return render(request,'post.html',context)

