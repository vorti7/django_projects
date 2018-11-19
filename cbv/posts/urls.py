from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('cbv/', views.CBView.as_view()),
    path('idv/', views.IndexView.as_view()),
    path('list/', views.SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetailView.as_view()),
    path('create/', views.SchoolCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
]
