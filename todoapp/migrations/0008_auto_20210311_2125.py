# Generated by Django 3.1.4 on 2021-03-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_auto_20210310_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtasks',
            old_name='subtasks',
            new_name='todo',
        ),
        migrations.AddField(
            model_name='subtasks',
            name='content',
            field=models.CharField(default='None', max_length=45),
        ),
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.CharField(default='None', max_length=45),
        ),
    ]
