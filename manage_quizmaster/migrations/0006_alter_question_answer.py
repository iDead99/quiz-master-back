# Generated by Django 5.0.6 on 2024-08-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_quizmaster', '0005_question_option1_question_option2_question_option3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
