from django.urls import path
from webapp import views


urlpatterns = [
    path('', views.IndexRedirectView.as_view(), name='redirect'),
    path('tasks', views.IndexView.as_view(), name='home'),
    path('projects/<int:project_id>/tasks/create', views.TaskCreateView.as_view(), name='tasks_create'),
    path('tasks/<int:id>', views.TaskDetailView.as_view(), name='tasks_detail'),
    path('tasks/<int:id>/update', views.TaskUpdateView.as_view(), name='tasks_update'),
    path('tasks/<int:id>/delete', views.TaskDeleteView.as_view(), name='tasks_delete'),
    path('projects', views.ProjectListView.as_view(), name='projects'),
    path('projects/create', views.ProjectCreateView.as_view(), name='projects_create'),
    path('projects/<int:id>', views.ProjectDetailView.as_view(), name='projects_detail'),
    path('projects/<int:id>/update', views.ProjectUpdateVIew.as_view(), name='projects_update'),
    path('projects/<int:id>/delete', views.ProjectDeleteView.as_view(), name='projects_delete'),
    path('projects/<int:project_id>/add_user', views.AddUserToProject.as_view(), name='add_user'),
    path('projects/<int:project_id>/delete_user/<int:user_id>', views.DeleteUserFromProject.as_view(), name='delete_user')
]