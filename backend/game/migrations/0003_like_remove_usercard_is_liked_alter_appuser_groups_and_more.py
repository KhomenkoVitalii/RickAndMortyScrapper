# Generated by Django 5.0.1 on 2024-02-07 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('game', '0002_appuser_is_staff_alter_appuser_country_and_more'),
        ('scrapper', '0008_alter_character_url_alter_episode_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usercard',
            name='is_liked',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='app_users', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='app_users', to='auth.permission'),
        ),
        migrations.AddIndex(
            model_name='appuser',
            index=models.Index(fields=['email'], name='game_appuse_email_6a86f1_idx'),
        ),
        migrations.AddIndex(
            model_name='appuser',
            index=models.Index(fields=['username'], name='game_appuse_usernam_47168a_idx'),
        ),
        migrations.AddIndex(
            model_name='usercard',
            index=models.Index(fields=['user'], name='game_userca_user_id_76118e_idx'),
        ),
        migrations.AddIndex(
            model_name='usercard',
            index=models.Index(fields=['character'], name='game_userca_charact_dcdf4f_idx'),
        ),
        migrations.AddField(
            model_name='like',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_obj', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user', 'content_type', 'object_id'), name='unique_like'),
        ),
    ]