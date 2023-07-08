

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Secretary, Lecturer

from django.db import transaction





class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')



class SecretarySignupForm(CustomUserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self, commit=True):
        user = super().save(commit=False)
        user.usertype = 1
        if commit:
            user.save()
            _secretary = Secretary.objects.create(
                user = user,
            )
            return user
        
class LecturerSignupForm(CustomUserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    @transaction.atomic
    def data_save(self, commit=True):
        user = super().save(commit=False)
        user.usertype = 1
        if commit:
            user.save()
            _lecturer = Lecturer.objects.create(
                user = user,
            )
            return user