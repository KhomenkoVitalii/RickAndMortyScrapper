from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from scrapper.models import Character
from django.contrib.contenttypes import fields, models as contrib_models


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
        user.is_staff = True

        user.save()

        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=56, unique=True, null=False)
    email = models.CharField(max_length=254, unique=True, null=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=58, null=True)
    image = models.ImageField(upload_to="uploads/images/users/", null=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['username'])
        ]

    objects = AppUserManager()

    groups = models.ManyToManyField(
        'auth.Group', related_name='app_users', blank=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='app_users', blank=True)

    def __str__(self):
        return self.username


class Like(models.Model):
    user = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name='main_user')

    content_type = models.ForeignKey(
        contrib_models.ContentType, on_delete=models.CASCADE, related_name='liked_obj')
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey()
    created_at = models.DateField(
        auto_now_add=True, null=False, editable=False)

    class Meta:
        indexes: [
            models.Index(fields=['user'])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'content_type', 'object_id'], name='unique_like')
        ]

    def __str__(self):
        return f"Like by {self.user.username} on {self.content_object}"


class UserCard(models.Model):
    user = models.ForeignKey(to=AppUser, on_delete=models.CASCADE)
    character = models.ForeignKey(to=Character, on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['character'])
        ]

    def __str__(self):
        return f"{self.user.username} owns {self.character.name}"
