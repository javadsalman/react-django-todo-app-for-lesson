# Generated by Django 4.1.3 on 2022-12-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_options_alter_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]
