# Generated by Django 2.2.16 on 2022-11-06 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20221105_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='description',
        ),
    ]
