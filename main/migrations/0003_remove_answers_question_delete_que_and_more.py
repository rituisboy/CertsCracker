# Generated by Django 4.2.3 on 2023-12-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_que_alter_answers_is_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.DeleteModel(
            name='QUE',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='text',
        ),
        migrations.AddField(
            model_name='questions',
            name='correct',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='optionA',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='optionB',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='optionC',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='optionD',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='questions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
