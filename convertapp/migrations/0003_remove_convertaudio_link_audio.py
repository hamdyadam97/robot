# Generated by Django 4.1 on 2022-10-05 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0002_convertaudio_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convertaudio',
            name='link_audio',
        ),
    ]