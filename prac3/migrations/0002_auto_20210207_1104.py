# Generated by Django 3.1.6 on 2021-02-07 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prac3', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_id',
            new_name='question',
        ),
    ]
