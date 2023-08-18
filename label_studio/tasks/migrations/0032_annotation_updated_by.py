# Generated by Django 3.2.16 on 2022-11-18 23:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0031_alter_task_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='updated_by',
            field=models.ForeignKey(help_text='Last user who updated this annotation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_annotations', to=settings.AUTH_USER_MODEL, verbose_name='updated by'),
        ),
    ]
