# Generated by Django 3.1.7 on 2021-12-02 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0001_initial'),
        ('Exercise_Category', '0001_initial'),
        ('Exercise_Day', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ex_Date', models.DateTimeField()),
                ('Ex_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise_Category.exercise_category')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise.exercise')),
            ],
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
    ]