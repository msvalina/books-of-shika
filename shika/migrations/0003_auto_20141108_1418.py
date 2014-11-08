# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shika', '0002_auto_20141106_0535'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LendingRecords',
            new_name='LendingRecord',
        ),
        migrations.AlterField(
            model_name='lendingrequest',
            name='is_confirmed',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
