# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 16:24
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
                ('bank', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_of_expenditure', models.DateField(default=django.utils.timezone.now)),
                ('comments', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('expense_type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('member_name', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=255)),
                ('date_of_income', models.DateField(default=django.utils.timezone.now)),
                ('earned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthly_expenses.Family')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('mode', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='expenditure',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenditure_category', to='monthly_expenses.Expense_category'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthly_expenses.Payment'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='spent_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthly_expenses.Family'),
        ),
        migrations.AddField(
            model_name='expenditure',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenditure_type', to='monthly_expenses.Expense_category'),
        ),
        migrations.AddField(
            model_name='cards',
            name='card_holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monthly_expenses.Family'),
        ),
    ]