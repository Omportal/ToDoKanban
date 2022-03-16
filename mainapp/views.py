from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Task
from django.urls import reverse
from .forms import Taskform


def task(request, task_id=1):
    all_objects = Task.objects.all()
    template = loader.get_template('mainapp/index.html')
    context = {
        'all_objects': all_objects,
    }
    return render(request, 'mainapp/index.html', context)


def card(request, task_title):
    one_card = Task.objects.filter(title=task_title)
    template = loader.get_template('mainapp/card.html')
    context = {
        'one_card': one_card,
    }
    return render(request, 'mainapp/card.html', context)


def create(request):
    error = ''
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Неправильно заполнена форма "

    form = Taskform()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/create.html', data)


def edit(request, task_title):
    obj = Task.objects.get(title=task_title)
    error = ''
    if request.method == "POST":
        form = Taskform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            error = "Неправильно заполнена форма "

    form = Taskform(instance=obj)
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/edit.html', data)
