# Generated by Django 5.0.6 on 2024-08-18 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_quizmaster', '0003_alter_quiz_date_to_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
