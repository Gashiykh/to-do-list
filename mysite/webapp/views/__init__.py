from django.views import generic

from webapp.views.task import (
    IndexView,
    TaskDetailView,
    TaskCreateView, 
    TaskUpdateView, 
    TaskDeleteView
    )
from webapp.views.project import (
    ProjectListView, 
    ProjectDetailView, 
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateVIew,
    )
from webapp.views.manage_users import (
    AddUserToProject,
    DeleteUserFromProject,
)

class IndexRedirectView(generic.RedirectView):
    pattern_name = 'projects'