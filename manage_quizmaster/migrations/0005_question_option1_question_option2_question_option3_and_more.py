# Generated by Django 5.0.6 on 2024-08-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_quizmaster', '0004_alter_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
