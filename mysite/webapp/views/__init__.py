from webapp.views.task import IndexView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from django.views import generic

class IndexRedirectView(generic.RedirectView):
    pattern_name = 'home'