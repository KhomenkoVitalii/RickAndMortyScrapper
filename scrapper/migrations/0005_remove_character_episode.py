# Generated by Django 4.2.7 on 2023-11-17 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0004_alter_character_image_alter_character_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='episode',
        ),
    ]
