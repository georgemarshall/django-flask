# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


def initial_data(apps, schema_editor):
    Question = apps.get_model('ex_django_rest', 'Question')

    q = Question.objects.create(question_text="What's up?", pub_date=timezone.now())
    q.choice_set.create(choice_text='Not much', votes=0)
    q.choice_set.create(choice_text='The sky', votes=0)
    q.choice_set.create(choice_text='Just hacking again', votes=0)


class Migration(migrations.Migration):

    dependencies = [
        ('ex_django_rest', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data),
    ]
