from django.contrib import admin
from .import models

@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    list_display=['phone', 'gender', 'user']
    list_per_page=10
    list_select_related = ['user']
    list_filter=['user']
    ordering=['gender', 'user']
    search_fields=['phone']

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display=['title', 'date_created', 'master']
    list_per_page=10
    list_select_related = ['master']
    list_filter=['date_created', 'master']
    ordering=['title', 'date_created']
    search_fields=['title', 'date_created']

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'quiz']
    list_per_page=10
    list_select_related = ['quiz']
    list_filter = ['answer', 'quiz']
    ordering=['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'quiz']
    search_fields=['question', 'option1', 'option2', 'option3', 'option4', 'answer']