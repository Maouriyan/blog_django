# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 11:06
from __future__ import unicode_literals

import autoslug.fields
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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tag_line', models.CharField(max_length=50)),
                ('short_description', models.TextField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('summary', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique_with=['blog'])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blog.Blog')),
            ],
        ),
    ]
