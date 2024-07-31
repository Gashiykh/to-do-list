from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse

from accounts.forms import MyUserCreationForm

# Create your views here.

def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        
        else:
            context['has_error'] = True

    return render(request, 'accounts/login.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('login')


class RegisterView(generic.CreateView):
    template_name = 'accounts/register.html'
    model = get_user_model()
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        
        if not next_url:
            next_url = self.request.GET.get('next')
        if not next_url:
            next_url = reverse('home')

        return next_url