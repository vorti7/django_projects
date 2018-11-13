from django.shortcuts import render, redirect
from secondapp.models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'secondapp/index.html',{'todos':todos})
def new(request):
    return render(request, 'secondapp/new.html')

def create(request):
    title = request.POST.get('title')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, deadline=deadline)
    todo.save()
    return redirect('/todos/')

def read(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'secondapp/read.html', {'todo':todo})
    
def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        deadline = request.POST.get('deadline')
        Todo.objects.create(title=title, deadline=deadline)
        return redirect('/todos/')
    else:
        return render(request, 'secondapp/todo_create.html')

def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == "POST":
        todo.title = request.POST.get('title')
        todo.deadline = request.POST.get('deadline')
        todo.save()
        return redirect('/todos/')
    else:
        deadline = todo.deadline.strftime("%Y-%m-%d")
        # deadline = "{}-{}-{}".format(todo.deadline.year,todo.deadline.month, todo.deadline.day)
        return render(request, 'secondapp/update.html', {'todo':todo, 'deadline':deadline})

def delete(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('/todos/')