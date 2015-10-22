# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('choice_text', models.CharField(verbose_name='choice text', max_length=200)),
                ('votes', models.IntegerField(verbose_name='votes', default=0)),
            ],
            options={'verbose_name': 'choice', 'verbose_name_plural': 'choices'},
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('question_text', models.CharField(verbose_name='question text', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='ex_django.Question', verbose_name='question'),
        ),
    ]
