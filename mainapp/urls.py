from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.TaskView.as_view(), name='main'),
    path('create/', views.create, name='create'),
    path('<int:task_id>/', views.card, name='card'),
    path('<int:task_id>/edit', views.edit, name='edit')
]
