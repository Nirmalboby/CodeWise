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

class SubmissionSerializer(serializers.Serializer):
    answer=serializers.CharField()
    question_id=serializers.IntegerField()
    points=serializers.IntegerField(read_only=True)
    owner=serializers.CharField()
    submission_date=serializers.DateTimeField(read_only=True)
    remarks=serializers.CharField(read_only=True)

    def validate(self,validated_data):
        question_id=validated_data.get("question_id")
        if not Questions.objects.filter(id=question_id).exists():
            raise serializers.ValidationError("Question Does Not Exist")
        return validated_data