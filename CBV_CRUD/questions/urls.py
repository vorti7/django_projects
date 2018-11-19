from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.QuestionListView.as_view(), name = 'list'),
    path('<int:pk>/', views.QuestionDetailView.as_view(), name = 'detail'),
    path('create/', views.QuestionCreateView.as_view(), name = 'create'),
    path('<int:pk>/update', views.QuestionUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete', views.QuestionDeleteView.as_view(), name = 'delete'),
    ]
