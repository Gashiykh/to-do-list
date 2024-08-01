from django.urls import path
from accounts import views
from django.contrib.auth import views as django_views
from accounts import views

urlpatterns = [
    path(
        'login',
        django_views.LoginView.as_view(
            template_name='accounts/login.html'
            ), name='login'
        ),
    path('logout', django_views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile/<int:id>', views.UserProfileView.as_view(), name='profile'),
    path('users', views.UserListView.as_view(), name='users_list')

]