# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shika', '0004_lendingrecord_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendingrequest',
            name='book_owner',
            field=models.ForeignKey(blank=True, to='shika.BookOwner', null=True),
            preserve_default=True,
        ),
    ]
