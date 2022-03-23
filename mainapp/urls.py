from django.urls import path
from . import views
from mainapp.views import RegisterView,TaskView

app_name = 'mainapp'

urlpatterns = [
    path('', TaskView.as_view(), name='main'),
    path('create/', views.create, name='create'),
    path('<int:task_id>/', views.card, name='card'),
    path('<int:task_id>/edit', views.edit, name='edit'),
    path('register/', RegisterView.as_view(), name="register")
]
