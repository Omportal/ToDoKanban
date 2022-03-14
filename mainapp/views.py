from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task


def index(request):
    return HttpResponse(f"Hello may canban project")


def task(request, task_id):
    all_objects = Task.objects.all()
    template = loader.get_template('mainapp/index.html')
    context = {
        'all_objects': all_objects,
    }
    return render(request, 'mainapp/index.html', context)

