# Generated by Django 4.2.7 on 2023-12-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='country',
            field=models.CharField(max_length=58, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/images/users/'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
