# Generated by Django 3.1.4 on 2021-01-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.CharField(max_length=60),
        ),
    ]
