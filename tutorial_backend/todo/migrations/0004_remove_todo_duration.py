# Generated by Django 4.1.3 on 2022-12-07 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='duration',
        ),
    ]
