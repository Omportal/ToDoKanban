from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.task, name='main'),
    path('<int:task_id>/', views.task, name='task'),
    path('create', views.create, name='create'),
    path('<str:task_title>/', views.card, name='card'),
    path('<str:task_title>/edit', views.edit, name='edit')
]
