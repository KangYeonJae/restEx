# Generated by Django 2.2 on 2019-10-29 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_post_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
    ]