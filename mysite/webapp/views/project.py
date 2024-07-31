from django.urls import reverse, reverse_lazy
from django.views import generic
from webapp.models import Project
from webapp.forms import ProjectForm
from django.contrib.auth.mixins import PermissionRequiredMixin



class ProjectListView(generic.ListView):
    template_name = 'projects/list.html'
    model = Project 
    context_object_name = 'projects'
    ordering = ['-started_at']


class ProjectDetailView(generic.DetailView):
    template_name = 'projects/detail.html'
    model = Project
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at').filter(is_deleted=False)
        context['tasks'] = tasks
        return context
    

class ProjectCreateView(PermissionRequiredMixin, generic.CreateView):
    template_name = 'projects/project.html'
    model = Project
    form_class = ProjectForm 
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.user.add(self.request.user)

        return response
    
    def get_success_url(self) -> str:
        return reverse('projects_detail', kwargs={'id': self.object.id})
    

class ProjectUpdateVIew(PermissionRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project.html'
    pk_url_kwarg = 'id'
    extra_context = {'title': 'Update Task', 'btn': 'Update'}
    permission_required = 'webapp.change_project'

    def get_success_url(self) -> str:
        return reverse('projects_detail', kwargs={'id':self.object.id})

class ProjectDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Project
    pk_url_kwarg = 'id'
    permission_required = 'webapp.delete_project'

    def get_success_url(self) -> str:
        return reverse_lazy('projects')