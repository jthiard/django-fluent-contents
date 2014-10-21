# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Slug')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleTextItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem')),
                ('text', models.TextField(verbose_name=b'Text')),
            ],
            options={
                'db_table': 'contentitem_article_articletextitem',
                'verbose_name': 'Article text item',
                'verbose_name_plural': 'Article text items',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
