# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 09:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_coach_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]