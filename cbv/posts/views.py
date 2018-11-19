from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

from .models import School

def index(request):
    return render(request, 'posts/index.html')

class CBView(View):
    def get(self, request):
        return HttpResponse("실행 완료 !!!")
class IndexView(TemplateView):
    template_name = 'posts/cbv_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = " H e l l o !"
        return context
        
class SchoolListView(ListView):
    template_name = 'posts/school_list.html'
    model = School

class SchoolDetailView(DetailView):
    template_name = 'posts/school_detail.html'
    model = School


class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'location')
    
class SchoolUpdateView(UpdateView):
    model = School
    fields = ('location',)
    
class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('posts:list')