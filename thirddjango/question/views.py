from django.shortcuts import render, resolve_url, redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    questions = paginator.get_page(page)
    
    return render(request, 'question/index.html', {'questions': questions})
    
@login_required
def create(request):
    if request.method =="POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = false)
            question.user = request.user
            question.save()
        return redirect(resolve_url("question:index"))
    else:
        form = QuestionForm()
        pass
    return render(request, 'question/create.html', {'form': form})
    
def read(request, id):
    question = Question.objects.get(id=id)
    form = CommentForm(initial={'question':id})
    anA = question.comment_set.all().filter(answer ='A')
    anB = question.comment_set.all().filter(answer ='B')
    
    if len(anA)+len(anB) == 0:
        anAper = 50
        anBper = 50
    else:
        anAper = len(anA)/(len(anA)+len(anB))*100
        anBper = len(anB)/(len(anA)+len(anB))*100
    return render(request, 'question/read.html', {'question': question, 'form': form, 'anA': anA, 'anB': anB, 'anAper': anAper, 'anBper': anBper})
    
def comment_create(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # form.save()
            comment = form.save(commit=False)
            comment.question = Question.objects.get(id=id)
            comment.save()
            return redirect(resolve_url('question:read', id))
    else:
        form = CommentForm()
        return redirect(resolve_url('question:read', id))
    return render(request, 'question/read.html', {'form':form})

def update(request, id):
    question = Question.objects.get(id=id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance = question)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('question:read', id))
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question/update.html', {'form': form,  'question': question})

def delete(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect(resolve_url('question:index'))
    
def comment_update(request, id, cid):
    comment = Comment.objects.get(id=cid)
    if request.method == "POST":
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('question:read', id))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'question/comment_update.html', {'form': form,  'comment': comment})
    
def comment_delete(request, id, cid):
    comment = Comment.objects.get(id=cid)
    comment.delete()
    return redirect(resolve_url('question:read', id))