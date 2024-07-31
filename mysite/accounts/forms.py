from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, label='Email address')
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
            )
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if not first_name and not last_name:
            raise forms.ValidationError('Either field (first_name, last_name) must be filled out.')
        
        return cleaned_data