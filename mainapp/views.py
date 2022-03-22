from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Task
from django.urls import reverse
from .forms import Taskform
from django.views import generic


class TaskView(generic.ListView):
    template_name = 'mainapp/index.html'
    context_object_name = "all_objects"

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user.id)
        return queryset


@login_required
def card(request, task_id):
    one_card = Task.objects.filter(id=task_id, user=request.user.id)
    template = loader.get_template('mainapp/card.html')
    context = {
        'one_card': one_card,
    }
    return render(request, 'mainapp/card.html', context)


@login_required
def create(request):
    error = ''
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect('/')
        else:
            error = "Неправильно заполнена форма "

    form = Taskform()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/create.html', data)


def edit(request, task_id):
    obj = Task.objects.get(id=task_id)
    error = ''
    if request.method == "POST":
        form = Taskform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            error = "Неправильно заполнена форма "

    form = Taskform(instance=obj)
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/edit.html', data)
