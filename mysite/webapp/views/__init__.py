from webapp.views.task import IndexView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.views import generic
from webapp.views.project import ProjectListView, ProjectDetailView, ProjectCreateView

class IndexRedirectView(generic.RedirectView):
    pattern_name = 'projects'