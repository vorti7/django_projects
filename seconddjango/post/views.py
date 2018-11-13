from django.shortcuts import render, redirect, resolve_url
from .forms import PostForm
from .models import Post

# Create your views here.
# def index(request):
#     return render(request, 'post/index.html')

def list(request):
    return render(request, 'post/list.html')
    
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