# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shika', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='book',
        ),
        migrations.RemoveField(
            model_name='reader',
            name='name',
        ),
        migrations.AlterField(
            model_name='lendingrecords',
            name='reader',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lendingrequest',
            name='reader',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Reader',
        ),
    ]
