# Generated by Django 2.2.16 on 2022-11-06 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20221106_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
