# Generated by Django 2.2.16 on 2022-11-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0021_comment_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
