# Generated by Django 4.1 on 2022-10-04 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('the_type', models.CharField(max_length=20)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
