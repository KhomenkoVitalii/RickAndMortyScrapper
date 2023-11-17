from django import forms
from django.contrib.auth.forms import UserCreationForm
from game.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        if self.cleaned_data['password1'] == self.cleaned_data['password2']:
            user = super(RegisterUserForm, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
