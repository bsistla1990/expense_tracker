# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 07:20
from __future__ import unicode_literals
import string,random

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_expenses', '0005_family_root'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='login_name',
            field=models.CharField(default=''.join(random.sample(string.ascii_lowercase, 10)), max_length=150, unique=True),
        ),
    ]
