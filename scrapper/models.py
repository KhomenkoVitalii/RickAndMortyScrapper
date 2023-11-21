from django.db import models
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=255, default="unknown")
    type = models.CharField(max_length=255, default="unknown")
    dimension = models.CharField(max_length=255, default="unknown")
    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)


class Character(models.Model):
    name = models.CharField(max_length=255, default="unknown")
    status = models.CharField(max_length=255, default="unknown")
    species = models.CharField(max_length=255, default="unknown")
    type = models.CharField(max_length=255, default="unknown")
    gender = models.CharField(max_length=255, default='unknown')
    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)

    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, null=True)

    image = models.ImageField(
        upload_to="uploads/images/character/", blank=True)

    episode = models.CharField(max_length=255)


class Origin(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    character_id = models.OneToOneField(Character, on_delete=models.CASCADE)


class Episode(models.Model):
    name = models.CharField(max_length=255)
    air_date = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)

    characters = models.ManyToManyField('Character', related_name='episodes')

    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)
