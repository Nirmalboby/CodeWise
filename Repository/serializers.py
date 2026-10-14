from rest_framework import serializers
from Repository.models import Questions

class QuestionSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=200)
    language=serializers.ChoiceField(choices=Questions.Languages,default="python")
    difficulty=serializers.ChoiceField(choices=Questions.Difficulty,default="easy")
    notes=serializers.CharField()
    topic=serializers.CharField()
    published_date=serializers.DateTimeField(read_only=True)
    sample_input=serializers.CharField()
    is_active=serializers.BooleanField()