from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index),
    path('new/',views.new),
    path('create/',views.create),
    path('<int:id>/', views.read),
    path('todo_create/',views.todo_create),
    path('<int:id>/update', views.update, name="update"),
    path('<int:id>/delete', views.delete, name="delete"),
]