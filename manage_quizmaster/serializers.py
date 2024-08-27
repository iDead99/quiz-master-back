from . import models
from rest_framework import serializers

class MasterSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.Master
        fields = ['id', 'user_id', 'gender', 'phone']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields = ['id', 'title', 'description', 'date_created', 'date_to_start', 'master']
        read_only_fields = ['master', 'date_created']

    def create(self, validated_data):
        user = self.context['request'].user
        master = models.Master.objects.get(user=user)
        validated_data['master'] = master
        return super().create(validated_data)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ['id', 'question','option1','option2','option3','option4', 'answer', 'quiz']

    def validate_quiz(self, value):
        user = self.context['request'].user

        try:
            master = models.Master.objects.get(user=user)
        except models.Master.DoesNotExist:
            raise serializers.ValidationError("No Quiz Master found.")
        
        if value.master != master:
            raise serializers.ValidationError("The selected Quiz does not belong to this Quiz Master.")

        return value