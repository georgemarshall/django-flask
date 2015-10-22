from tastypie import fields
from tastypie.resources import ModelResource

from .models import Question, Choice


class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'


class QuestionResource(ModelResource):
    choices = fields.ToManyField(ChoiceResource, 'choice_set', full=True)

    class Meta:
        queryset = Question.objects.all()
        resource_name = 'question'
