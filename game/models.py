from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from scrapper.models import Character


class AppUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('An username is required!')
        if not email:
            raise ValueError('An email is required!')
        if not password:
            raise ValueError('An password is required!')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if not username:
            raise ValueError('An username is required!')
        if not email:
            raise ValueError('An email is required!')
        if not password:
            raise ValueError('An password is required!')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=56, unique=True, null=False)
    email = models.CharField(max_length=254, unique=True, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=58)
    image = models.ImageField(upload_to="uploads/images/users/")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()

    def __str__(self):
        return self.username


class UserCard(models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=models.CASCADE)
    character = models.ForeignKey(to=Character, on_delete=models.DO_NOTHING)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} owns {self.character.name}"
