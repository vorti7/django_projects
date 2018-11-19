from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm, PostModelForm
from .models import Post

# Create your views here.
# def index(request):
#     return render(request, 'post/index.html')

def list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts':posts})
    
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data['title']
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            Post.objects.create(title=title, content=content)
            
            return redirect(resolve_url('post:list'))
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form':form})
    
def detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'post/detail.html',{'post':post})
    
def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            # post.update(title=title, content=content)
            post.title = title
            post.content = content
            post.save()
            return redirect(resolve_url('post:detail', id))
    else:
        form = PostForm({'title':post.title, 'content':post.content})
    return render(request, 'post/update.html', {'post':post, 'form': form})
    
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(resolve_url('post:list'))

def model_create(request):
    if request.method == "POST":
        pass
    else:
        form = PostModelForm()
        pass
    return render(request, 'post/model_create.html', {'form':form})

def model_update(request, id):
    pass