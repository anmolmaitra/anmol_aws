# Generated by Django 3.1.7 on 2022-01-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise_Day', '0002_auto_20211202_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise_day',
            old_name='Name',
            new_name='exercise',
        ),
        migrations.RemoveField(
            model_name='exercise_day',
            name='Ex_Category',
        ),
    ]
