from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:id>/read/', views.read, name = 'read'),
    path('<int:id>/comment/create/', views.comment_create, name = 'comment_create'),
    path('<int:id>/update/', views.update, name = 'update'),
    path('<int:id>/delete/', views.delete, name = 'delete'),
    path('<int:id>/<int:cid>/comment_update/', views.comment_update, name = 'comment_update'),
    path('<int:id>/<int:cid>/comment_delete/', views.comment_delete, name = 'comment_delete'),
]