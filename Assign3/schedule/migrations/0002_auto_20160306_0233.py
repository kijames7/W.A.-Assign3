# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classschedule',
            name='credit_hour',
            field=models.CharField(max_length=1, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='days',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='location',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='section_number',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='classschedule',
            name='times',
            field=models.CharField(max_length=11, null=True, blank=True),
        ),
    ]
