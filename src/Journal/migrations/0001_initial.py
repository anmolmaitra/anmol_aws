# Generated by Django 3.1.7 on 2021-03-16 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JEntry', models.TextField()),
                ('IsVisible', models.BooleanField()),
                ('entryDt', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
