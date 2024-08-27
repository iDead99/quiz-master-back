from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from . import models, serializers
from django.conf import settings

class MasterViewSet(viewsets.ModelViewSet):
    # queryset = models.Master.objects.all()
    serializer_class = serializers.MasterSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return models.Master.objects.all()
        user_id=self.request.user.id
        return models.Master.objects.filter(user_id=user_id)

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        master = models.Master.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = serializers.MasterSerializer(master)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.MasterSerializer(master, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuizSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'date_to_start']
    search_fields = ['title', 'description', 'date_to_start']

    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return models.Quiz.objects.all()
        master_id=models.Master.objects.only('id').get(user_id=user.id)
        return models.Quiz.objects.filter(master_id=master_id).order_by('-date_created')
    
class QuestionViewSet(viewsets.ModelViewSet):
    # queryset = models.Question.objects.select_related('quiz').all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['quiz__id']
    search_fields = ['question', 'answer', 'option1', 'option2', 'option3', 'option4']

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['quiz__id']
    search_fields = ['question', 'answer', 'option1', 'option2', 'option3', 'option4']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            # If the user is a staff member, return all questions
            return models.Question.objects.all()
        else:
            # Get the current master's quizzes
            master = get_object_or_404(models.Master, user=user)
            quizzes = models.Quiz.objects.filter(master=master).values_list('id', flat=True)
            # Return only the questions associated with the master's quizzes
            return models.Question.objects.filter(quiz__id__in=quizzes)
