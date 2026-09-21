import os
from uuid import uuid4
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


def path_to_images_instruction(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join('instructions', filename)


class InstructionCard(models.Model):
    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        ordering = 'order',

    image = models.ImageField(upload_to=path_to_images_instruction, blank=False, verbose_name='Картинка')
    text_1 = RichTextUploadingField(blank=True, verbose_name='Текст')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')


class QuestionInstruction(models.Model):
    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'
        ordering = 'order',

    title = models.CharField(max_length=500, blank=False, verbose_name='Вопрос')
    text = RichTextUploadingField(blank=False, verbose_name='Ответ')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')


class ExpertAdvice(models.Model):
    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы эксперта'
        ordering = 'order',

    TYPE = [
        ('block_1', 'Блок 1'),
        ('mistakes', 'Распространенные ошибки'),
        ('block_2', 'Блок 2'),
    ]

    text = RichTextUploadingField(blank=False, verbose_name='Текст')
    block = models.CharField(max_length=100, default='block_1', choices=TYPE, verbose_name='Блок отображения')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
