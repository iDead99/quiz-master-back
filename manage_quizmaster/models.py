from django.db import models
from django.contrib import admin
from django.conf import settings

class Master(models.Model):
    phone = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_to_start = models.DateTimeField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=500, blank=True)
    option2 = models.CharField(max_length=500, blank=True)
    option3 = models.CharField(max_length=500, blank=True)
    option4 = models.CharField(max_length=500, blank=True)
    answer = models.CharField(max_length=255, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question