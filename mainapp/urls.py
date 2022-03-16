from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.TaskView.as_view(), name='main'),
    path('create/', views.create, name='create'),
    path('<str:task_title>/', views.card, name='card'),
    path('<str:task_title>/edit', views.edit, name='edit')
]
