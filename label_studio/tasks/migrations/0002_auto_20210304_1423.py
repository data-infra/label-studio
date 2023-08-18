# Generated by Django 3.1.4 on 2021-03-04 14:23
import django
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('io_storages', '0001_squashed_0002_auto_20210302_1827'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_squashed_0041_taskcompletionhistory_was_cancelled'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskCompletion',
            new_name='Annotation',
        ),
        migrations.RenameModel(
            old_name='TaskCompletionDraft',
            new_name='AnnotationDraft',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='completion',
            new_name='annotation',
        ),
        migrations.RenameField(
            model_name='annotationdraft',
            old_name='completion',
            new_name='annotation',
        ),
        migrations.AlterField(
            model_name='annotationdraft',
            name='annotation',
            field=models.ForeignKey(blank=True, help_text='Corresponding annotation for this draft', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drafts', to='tasks.annotation'),
        ),
        migrations.AlterField(
            model_name='task',
            name='file_upload',
            field=models.ForeignKey(blank=True, help_text='Uploaded file used as data source for this task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='data_import.fileupload'),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_labeled',
            field=models.BooleanField(default=False, help_text='True if the annotation number for this task is greater or equal to the project maximum_annotations', verbose_name='is_labeled'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='completed_by',
            field=models.ForeignKey(help_text='User ID who made this annotation', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annotations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='honeypot',
            field=models.BooleanField(default=False, help_text='This annotation is Ground Truth (honeypot)', verbose_name='honeypot'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='lead_time',
            field=models.FloatField(default=None, help_text='How much time spent to solve the annotation', null=True, verbose_name='lead time'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='prediction',
            field=models.JSONField(default=dict, help_text='Prediction viewed at the time of annotation', null=True, verbose_name='prediction'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='prediction_equal_score',
            field=models.FloatField(default=0.0, help_text='Comparison result with prediction viewed at the time of annotation', verbose_name='prediction_equal_score'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='result_count',
            field=models.IntegerField(default=0, help_text='Results inside of annotation counter', verbose_name='result count'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='task',
            field=models.ForeignKey(help_text='Corresponding task for this annotation', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='annotations', to='tasks.task'),
        ),
        migrations.AlterField(
            model_name='annotationdraft',
            name='lead_time',
            field=models.FloatField(help_text='how much time spent to solve the annotation', verbose_name='lead time'),
        ),
    ]
