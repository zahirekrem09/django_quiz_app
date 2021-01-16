from rest_framework import serializers
from .models import Answer, Category, Question, Quiz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'quiz_count')


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'question_count')

# nesdet serilaizer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    difficulty = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('title', 'difficulty', 'answer')

    def get_difficulty(self, obj):
        return obj.get_difficulty_display()
