from typing import Any
from urllib.parse import urlencode
from django.http import Http404, HttpResponseRedirect
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from webapp.models import Task
from webapp.forms import TaskForm, SearchForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    template_name = 'tasks/list.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 10

    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()

        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        if not context['tasks']:
            context['message'] = "Задачи не найдены."
        
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        queryset = queryset.filter(is_deleted=False)
        return queryset


    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None



class TaskDetailView(generic.DetailView):
    pk_url_kwarg = 'id'
    model = Task
    template_name = 'tasks/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Задача не найдена")
        return obj
    

class TaskCreateView(LoginRequiredMixin, generic.CreateView):

    template_name = 'tasks/task.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        project_id = self.kwargs.get('project_id')
        task = form.save(commit=False)
        task.project_id = project_id
        task.save()
        types = form.cleaned_data['types']
        task.types.set(types)

        return redirect('projects_detail', id=project_id)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
        
    template_name = 'tasks/task.html'
    form_class = TaskForm
    model = Task
    context_key = 'task'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('projects_detail', kwargs={'id': self.object.project.id})
 
class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse('projects_detail', kwargs={'id': self.object.project.id})
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True  
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.is_deleted:
            raise Http404("Задача не найдена")
        return obj
