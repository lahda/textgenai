# Generated by Django 4.2.4 on 2023-08-31 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recordings',
            new_name='Recording',
        ),
    ]