import os

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from pathlib import Path
from uuid import uuid4


def path_to_faq_categories_icons(instance, filename):
    if filename.endswith('.svg'):
        return os.path.join('faq_icons', filename)
    else:
        filename = f"{uuid4()}.webp"
        return os.path.join('faq_icons', filename)


class CategoryFaq(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = 'order',

    title = models.CharField(max_length=500, blank=False, verbose_name='Заголовок')
    icon = models.FileField(upload_to=path_to_faq_categories_icons, blank=False, verbose_name='Иконка')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            current_category_faq = CategoryFaq.objects.get(pk=self.pk)

            if self.icon:
                try:
                    if current_category_faq.icon and current_category_faq.icon != self.icon:
                        current_category_faq_path = Path(current_category_faq.icon.path)
                        if current_category_faq_path.exists():
                            current_category_faq_path.unlink()
                except CategoryFaq.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class QuestionFaq(models.Model):
    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'
        ordering = 'order',

    title = models.CharField(max_length=500, blank=False, verbose_name='Вопрос')
    text = RichTextUploadingField(blank=False, verbose_name='Ответ')
    category_faq = models.ForeignKey(CategoryFaq, blank=False, on_delete=models.CASCADE, verbose_name='Категория', related_name='questions')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')