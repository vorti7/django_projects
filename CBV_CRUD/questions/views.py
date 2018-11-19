from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'questions/index.html')
class QuestionListView(ListView):
    template_name = 'questions/question_list.html'
    model = Question
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/question_detail.html'
class QuestionCreateView(CreateView):
    model = Question
    fields = ("title", "ansA", "ansB")
class QuestionUpdateView(UpdateView):
    model = Question
    fields = ("title", "ansA", "ansB")
    
class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('questions:list')