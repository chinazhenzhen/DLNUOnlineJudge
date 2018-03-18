# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(db_index=True, max_length=24)),
                ('is_public', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('input_description', models.TextField()),
                ('output_description', models.TextField()),
                ('hint', models.TextField()),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('source', models.CharField(max_length=200)),
                ('submit_number', models.BigIntegerField(default=0)),
                ('accepted_number', models.BigIntegerField(default=0)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem',
                'ordering': ('create_time',),
            },
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'problem_tag',
            },
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(to='problem.ProblemTag'),
        ),
        migrations.AlterUniqueTogether(
            name='problem',
            unique_together=set([('id',)]),
        ),
    ]