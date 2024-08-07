# Generated by Django 5.0.6 on 2024-06-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_trainer', models.CharField(max_length=20)),
                ('course_careers', models.SmallIntegerField()),
                ('course_id', models.CharField(max_length=15)),
                ('course_description', models.CharField(max_length=50)),
                ('course_score', models.CharField(max_length=20)),
                ('course_duration', models.PositiveBigIntegerField()),
                ('course_sessions', models.CharField(max_length=20)),
                ('course_students', models.PositiveBigIntegerField()),
            ],
        ),
    ]
