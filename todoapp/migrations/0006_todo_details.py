# Generated by Django 3.1.4 on 2021-02-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_todo_is_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='details',
            field=models.TextField(default='None'),
        ),
    ]