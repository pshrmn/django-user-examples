# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=50)),
                ('b', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='pair',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aorb.Pair'),
        ),
    ]
