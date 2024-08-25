# Generated by Django 5.1 on 2024-08-24 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='code',
            new_name='course_code',
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
