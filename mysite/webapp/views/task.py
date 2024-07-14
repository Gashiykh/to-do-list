from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from webapp.models import Task
from webapp.forms import TaskForm


class IndexView(generic.TemplateView):
    template_name = 'tasks/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()

        return context

 
class TaskDetailView(generic.TemplateView):
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, id=self.kwargs.get('id'))

        return context
    

class TaskCreateView(generic.FormView):

    template_name = 'tasks/task.html'
    form_class = TaskForm

    
    def form_valid(self, form):
        types = form.cleaned_data.pop('types')

        self.task = Task.objects.create(
            title=form.cleaned_data.get('title'),
            description=form.cleaned_data.get('description'),
            status=form.cleaned_data.get('status'),
        )

        self.task.types.set(types)


        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks_detail',  kwargs={'id': self.task.id})


class TaskUpdateView(generic.FormView):
        
    template_name = 'tasks/task.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task

        return context
    
    def get_initial(self):
        initial = {}
        for key in 'title', 'description', 'status':
            initial[key] = getattr(self.task, key)
        initial['types'] = self.task.types.all()
        return initial

    def form_valid(self, form):
        data = form.cleaned_data

        self.task.title = data.get('title')
        self.task.description = data.get('description')
        self.task.status = data.get('status')
        self.task.types.set(data.get('types'))
        self.task.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks_detail', kwargs={'id': self.task.id})

    def get_object(self):
        return get_object_or_404(Task, id=self.kwargs.get('id'))

 
class TaskDeleteView(generic.View):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id).delete()
        return redirect('home')
