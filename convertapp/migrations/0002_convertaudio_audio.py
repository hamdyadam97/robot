# Generated by Django 4.1 on 2022-10-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='convertaudio',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
    ]