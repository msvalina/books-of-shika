# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shika', '0003_auto_20141108_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendingrecord',
            name='request',
            field=models.ForeignKey(default=1, to='shika.LendingRequest'),
            preserve_default=False,
        ),
    ]
