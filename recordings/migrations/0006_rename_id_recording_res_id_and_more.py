# Generated by Django 4.2.4 on 2023-09-08 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0005_recording_extend_recording_rewrite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recording',
            old_name='id',
            new_name='res_id',
        ),
        migrations.RenameField(
            model_name='recording_extend',
            old_name='id',
            new_name='ext_id',
        ),
        migrations.RenameField(
            model_name='recording_rewrite',
            old_name='id',
            new_name='rew_id',
        ),
    ]
