from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.changed_data('email')
        if commit:
            user.save()
        return user
