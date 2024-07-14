from django import forms
from django.forms import widgets
from webapp.models import Task, Status, Type
from django.core import validators
from django.utils.deconstruct import deconstructible


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

class TaskFormOld(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Action',
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(50),
        ],
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
        queryset=Type.objects.all(),
        required=True,
        label='Type',
        widget=widgets.CheckboxSelectMultiple
    )


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