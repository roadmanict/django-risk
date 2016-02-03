# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 14:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20160127_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default='unnamed', max_length=255),
        ),
        migrations.AlterField(
            model_name='riskprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='risk_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]