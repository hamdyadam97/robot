# Generated by Django 4.1 on 2022-10-05 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertapp', '0003_remove_convertaudio_link_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='convertaudio',
            name='image',
            field=models.ImageField(default=0.0001234567901234568, upload_to='audio'),
            preserve_default=False,
        ),
    ]