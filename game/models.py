from django.db import models
from django.contrib.auth.models import User
from scrapper.models import Character

# Create your models here.


class UserCard(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    character_id = models.ForeignKey(to=Character, on_delete=models.DO_NOTHING)
    is_liked = models.BooleanField(default=False)
