from django.core import validators
from django.utils.deconstruct import deconstructible
from django import forms
from django.forms import widgets
from django.contrib.auth import get_user_model

from webapp.models import Task, Project, ProjectUser



@deconstructible
class MinLengthValidator(validators.BaseValidator):
    message = 'min length must be 10'
    code = 'short_text'

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)
    
class MaxLengthValidator(validators.BaseValidator):
    message = 'max length must be 50'
    code = 'long_text'

    def compare(self, value, limit):
        return value > limit

    def clean(self, value):
        return len(value)




class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Action',
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(50),
        ],
    )



    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'types']
        exclude = ['is_deleted']
        widgets = {
            'types': forms.CheckboxSelectMultiple,
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'started_at', 'ended_at']    

    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')


class ProjectUserForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label='Пользователь')

    class Meta:
        model = ProjectUser
        fields = ['user']
    
