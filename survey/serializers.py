from rest_framework import serializers
from .models import Question, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Question
<<<<<<< HEAD
        fields = ["question_text", "pub_date", "choices"]
=======
        fields = ['question_text', 'pub_date', 'choices']
>>>>>>> 17e482e7b18bc60b63f7d48788237b22c270d5e1



