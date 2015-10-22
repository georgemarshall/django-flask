from rest_framework import serializers

from .models import Choice, Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(source='choice_set', many=True)

    class Meta:
        model = Question
