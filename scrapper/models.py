from django.db import models
from django.utils import timezone


class Location(models.Model):
    name = models.CharField(max_length=255, default="unknown", unique=True)
    type = models.CharField(max_length=255, default="unknown", blank=True)
    dimension = models.CharField(max_length=255, default="unknown", blank=True)
    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)


class Character(models.Model):
    name = models.CharField(max_length=255, default="unknown")
    status = models.CharField(max_length=255, default="unknown")
    species = models.CharField(max_length=255, default="unknown")
    type = models.CharField(max_length=255, default="unknown", blank=True)
    gender = models.CharField(max_length=255, default='unknown')
    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)

    location = models.ForeignKey(
        Location, on_delete=models.DO_NOTHING, null=True)

    image = models.ImageField(
        upload_to="uploads/images/character/", blank=True)


class Origin(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    character_id = models.OneToOneField(Character, on_delete=models.CASCADE)
    location = models.ForeignKey(
        to=Location, on_delete=models.DO_NOTHING, null=True, default=None)


class Episode(models.Model):
    name = models.CharField(max_length=25)
    air_date = models.CharField(max_length=255)
    episode = models.CharField(max_length=255, unique=True)

    characters = models.ManyToManyField('Character', related_name='episodes')

    url = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now, editable=False)
