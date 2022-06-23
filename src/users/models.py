from django import forms
from django.db import models
from django.contrib.auth.models import User
# from .models import Profile


def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models. OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_profile_path, default="avatar.png")
    bio = models.TextField(blank=True)

    def __str__(self):
        return "{} Profile".format(self.user)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image", "bio")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")    