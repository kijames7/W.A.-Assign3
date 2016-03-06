# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('student_name', models.CharField(max_length=80, null=True, blank=True)),
                ('professor_name', models.CharField(max_length=80, null=True, blank=True)),
                ('course_name', models.CharField(max_length=80, null=True, blank=True)),
                ('student_id', models.CharField(max_length=80, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
