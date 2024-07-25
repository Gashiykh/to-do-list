from typing import Any
from django.urls import reverse
from django.views import generic
from webapp.models import Project
from webapp.forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ProjectListView(generic.ListView):
    template_name = 'projects/list.html'
    model = Project 
    context_object_name = 'projects'
    ordering = ['-started_at']


class ProjectDetailView(generic.DeleteView):
    template_name = 'projects/detail.html'
    model = Project
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at')
        context['tasks'] = tasks
        return context
    

class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'projects/project.html'
    model = Project
    form_class = ProjectForm 
    
    def get_success_url(self) -> str:
        return reverse('projects_detail', kwargs={'id': self.object.id})