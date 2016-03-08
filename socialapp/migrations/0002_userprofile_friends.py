# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='_userprofile_friends_+', to='socialapp.UserProfile'),
        ),
    ]