from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import ProjectUser, Project
from webapp.forms import ProjectUserForm


class AddUserToProject(PermissionRequiredMixin, generic.CreateView):
    model = ProjectUser
    template_name = 'projects/manage_user.html'
    form_class = ProjectUserForm
    permission_required = 'accounts.add_user'

    def has_permission(self) -> bool:
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        return super().has_permission() and ProjectUser.objects.filter(project=project, user=self.request.user).exists()

    def form_valid(self, form):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        user = form.cleaned_data['user']
        ProjectUser.objects.get_or_create(project=project, user=user)

        return redirect('projects_detail', id=project.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_id'])
        return context

    
class DeleteUserFromProject(PermissionRequiredMixin, generic.DeleteView):
    model = ProjectUser
    permission_required = 'accounts.delete_user'

    def has_permission(self) -> bool:
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        return super().has_permission() and ProjectUser.objects.filter(project=project, user=self.request.user).exists()

    def get_object(self):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        user_obj = get_object_or_404(get_user_model(), id=self.kwargs['user_id'])
        return get_object_or_404(ProjectUser, project=project, user=user_obj)

    def delete(self, request, *args, **kwargs):
        user_obj = self.get_object()
        user_obj.delete()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('projects_detail', kwargs={'id': self.kwargs['project_id']})


    
    

