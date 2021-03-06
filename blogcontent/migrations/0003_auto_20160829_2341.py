# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogcontent', '0002_auto_20160807_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='timeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('year', 'year'), ('month', 'month'), ('week', 'week'), ('day', 'day')], default='unknownTime', max_length=5)),
                ('time', models.DateField()),
                ('todoList', models.CharField(max_length=2000)),
                ('doneList', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='blog_content',
        ),
    ]
