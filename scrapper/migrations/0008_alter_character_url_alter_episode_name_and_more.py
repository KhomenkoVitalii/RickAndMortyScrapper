# Generated by Django 4.2.7 on 2023-11-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0007_alter_character_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='episode',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
