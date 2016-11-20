# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('finalization_date', models.DateTimeField(blank=True, null=True)),
                ('priority', models.PositiveSmallIntegerField(default=0)),
                ('difficulty', models.PositiveSmallIntegerField(default=0)),
                ('project', models.ForeignKey(to='todo_list.proyecto', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
        ),
    ]
