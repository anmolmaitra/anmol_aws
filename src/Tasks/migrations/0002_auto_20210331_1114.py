# Generated by Django 3.1.7 on 2021-03-31 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='taskStatus',
            field=models.ForeignKey(default='NOT STARTED', on_delete=django.db.models.deletion.CASCADE, to='Tasks.taskstatus'),
        ),
    ]
