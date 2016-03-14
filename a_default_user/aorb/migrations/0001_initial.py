# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 21:36
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
        migrations.AddField(
            model_name='choice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]