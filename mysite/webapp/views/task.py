from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from webapp.models import Task
from webapp.forms import TaskForm


class IndexView(generic.TemplateView):
    template_name = 'tasks/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()

        return context

 
class TaskDetailView(generic.TemplateView):
    template_name = 'tasks/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, id=self.kwargs.get('id'))

        return context
    

class TaskCreateView(generic.View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/create.html', context={'form': form})
    
    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task = Task.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
            )

            task.types.set(types)
            return redirect('tasks_detail', id=task.id)
        else:
            return render(request, 'tasks/create.html', context={'form': form})


class TaskUpdateView(generic.View):
    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        
        return render(
            request, 'tasks/update.html', 
            context={'task': task, 'form': TaskForm(initial={
                **vars(task),
                'types': task.types.all(),
            })},
        )
    
    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        form = TaskForm(data=request.POST)

        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.types.set(request.POST.get('types'))

            task.save()
            return redirect('tasks_detail', id=task.id)
        else:
            return render(request, 'tasks/update.html', context={'form': form, 'task': task})
        

class TaskDeleteView(generic.View):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id).delete()
        return redirect('home')
