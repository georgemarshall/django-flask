from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(_('question text'), max_length=200)
    pub_date = models.DateTimeField(_('date published'))

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('questions')


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, verbose_name=_('question'))
    choice_text = models.CharField(_('choice text'), max_length=200)
    votes = models.IntegerField(_('votes'), default=0)

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choices')
