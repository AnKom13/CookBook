# Generated by Django 5.0.1 on 2024-01-15 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category', verbose_name='Категория')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]