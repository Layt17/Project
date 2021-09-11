from django.db import models
from django.contrib.auth import get_user_model

import datetime

class Question(models.Model):

        class Type:
            TEXT = 'TEXT'
            CHOICE = 'CHOICE'
            MULTICHOICE = 'MULTICHOICE'

            choices = (
                (TEXT, 'TEXT'),
                (CHOICE, 'CHOICE'),
                (MULTICHOICE, 'MULTICHOICE'),
            )

        quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, verbose_name='Опрос №')
        text = models.CharField(max_length=255, verbose_name='текст вопроса')
        type = models.CharField(max_length=255, choices=Type.choices, default=Type.TEXT, verbose_name='Тип ответа')

        def __str__(self):
            return self.quiz

        class Meta:
            verbose_name = 'Вопрос'
            verbose_name_plural = 'Вопросы'


class Choice(models.Model):

    question = models.ForeignKey('Question', related_name='choices', on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(max_length=100, default='Enter value')

    def __str__(self):
        return self.question.quiz.title

    class Meta:
        verbose_name = 'Вобор'
        verbose_name_plural = 'Выборы'


class Quiz(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название опроса')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'



class Solution(models.Model):

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Опрос №')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    date = models.DateField(default=datetime.date.today(), editable=False, verbose_name='Дата')

    def __str__(self):
        return '{} : {}'.format(self.quiz, self.user)

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'



class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    solution = models.ForeignKey(Solution, related_name='answers', on_delete=models.CASCADE, verbose_name='Решение')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='Выбор')
    value = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return '{} : {}'.format(self.question, self.choice)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


