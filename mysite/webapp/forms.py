from django import forms
from django.forms import widgets
from .models import Task, Status, Type
from webapp import models

class TaskForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Action'
        )
    description = forms.CharField(
        max_length=3000,
        required=False,
        label='Description',
        widget=widgets.Textarea
        )
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=True,
        label='Status'
        )
    types = forms.ModelMultipleChoiceField(
        queryset=models.Type.objects.all(),
        required=True,
        label='Type',
        widget=widgets.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'types']

