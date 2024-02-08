from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Character)
admin.site.register(models.Location)
admin.site.register(models.Episode)
