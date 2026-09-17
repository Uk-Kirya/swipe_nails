import os

from django.db import models
from django.utils.text import slugify
from pathlib import Path
from uuid import uuid4
from ckeditor_uploader.fields import RichTextUploadingField


def path_to_category_cover(instance, filename):
    if filename.endswith('.svg'):
        return os.path.join('categories', filename)
    else:
        filename = f"{uuid4()}.webp"
        return os.path.join('categories', filename)


def path_to_product_images(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join(f'products', filename)


def path_to_video(instance, filename):
    return os.path.join(f'videos', filename)


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    cover = models.ImageField(upload_to=path_to_category_cover, blank=False, verbose_name='Обложка')
    icon = models.FileField(upload_to=path_to_category_cover, blank=False, verbose_name='Иконка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    animation = models.IntegerField(default=0, blank=True, verbose_name='Анимация загрузки (м.сек)')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')

    keywords = models.TextField(blank=True, verbose_name='Keywords')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.pk:
            current_category = Category.objects.get(pk=self.pk)

            if self.cover:
                try:
                    if current_category.cover and current_category.cover != self.cover:
                        cover_path = Path(current_category.cover.path)
                        if cover_path.exists():
                            cover_path.unlink()
                except Category.DoesNotExist:
                    pass

            if self.icon:
                try:
                    if current_category.icon and current_category.icon != self.icon:
                        icon_path = Path(current_category.icon.path)
                        if icon_path.exists():
                            icon_path.unlink()
                except Category.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Style(models.Model):
    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'
        ordering = ['order']

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    cover = models.ImageField(upload_to=path_to_category_cover, blank=False, verbose_name='Обложка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    animation = models.IntegerField(default=0, blank=True, verbose_name='Анимация загрузки (м.сек)')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')

    keywords = models.TextField(blank=True, verbose_name='Keywords')
    description = models.TextField(blank=True, verbose_name='Description')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.pk:
            current_style = Style.objects.get(pk=self.pk)

            if self.cover:
                try:
                    if current_style.cover and current_style.cover != self.cover:
                        cover_path = Path(current_style.cover.path)
                        if cover_path.exists():
                            cover_path.unlink()
                except Style.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        ordering = 'title',

    title = models.CharField(max_length=255, blank=False, verbose_name='Цвет')

    def __str__(self):
        return self.title


class AccessoriesCategory(models.Model):
    class Meta:
        verbose_name = 'Категория Аксессуаров'
        verbose_name_plural = 'Категории Аксессуаров'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    cover = models.ImageField(upload_to=path_to_category_cover, blank=False, verbose_name='Обложка')
    text = RichTextUploadingField(blank=True, verbose_name='Текст')
    animation = models.IntegerField(default=0, blank=True, verbose_name='Анимация загрузки (м.сек)')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
    keywords = models.TextField(blank=True, verbose_name='Keywords')
    description = models.TextField(blank=True, verbose_name='Description')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.pk:
            current_category = AccessoriesCategory.objects.get(pk=self.pk)

            if self.cover:
                try:
                    if current_category.cover and current_category.cover != self.cover:
                        cover_path = Path(current_category.cover.path)
                        if cover_path.exists():
                            cover_path.unlink()
                except AccessoriesCategory.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Product(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    TYPE = [
        ('product', 'Обычный продукт'),
        ('combo', 'Комбо-набор'),
        ('accessories', 'Аксессуар'),
    ]

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    cover_1 = models.ImageField(upload_to=path_to_product_images, blank=False, verbose_name='Картинка 1')
    cover_2 = models.ImageField(upload_to=path_to_product_images, blank=False, verbose_name='Картинка 2')
    video = models.FileField(upload_to=path_to_product_images, blank=True, verbose_name='Видео')
    price = models.IntegerField(default=0, blank=False, verbose_name='Стоимость (₸)')
    type = models.CharField(max_length=100, default='product', choices=TYPE, verbose_name='Тип товара')
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    style = models.ForeignKey(Style, blank=True, on_delete=models.CASCADE, verbose_name='Стиль', related_name='products')
    color = models.ForeignKey(Color, blank=True, on_delete=models.CASCADE, verbose_name='Цвет', related_name='products')
    acessories = models.ForeignKey(AccessoriesCategory, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Категория аксессура', related_name='products')
    text_1 = RichTextUploadingField(blank=True, verbose_name='Текст')
    text_2 = RichTextUploadingField(blank=True, verbose_name='Описание')
    text_3 = RichTextUploadingField(blank=True, verbose_name='Как оплатить')
    text_4 = RichTextUploadingField(blank=True, verbose_name='Покупка и возврат')
    text_5 = RichTextUploadingField(blank=True, verbose_name='FAQ')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    popular = models.BooleanField(default=False, verbose_name='Популярный?')
    new = models.BooleanField(default=False, verbose_name='Новинка?')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
    keywords = models.TextField(blank=True, verbose_name='Keywords')
    description = models.TextField(blank=True, verbose_name='Description')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.pk:
            current_product = Product.objects.get(pk=self.pk)

            if self.cover_1:
                try:
                    if current_product.cover_1 and current_product.cover_1 != self.cover_1:
                        cover_1_path = Path(current_product.cover_1.path)
                        if cover_1_path.exists():
                            cover_1_path.unlink()
                except Product.DoesNotExist:
                    pass

            if self.cover_2:
                try:
                    if current_product.cover_2 and current_product.cover_2 != self.cover_2:
                        cover_2_path = Path(current_product.cover_2.path)
                        if cover_2_path.exists():
                            cover_2_path.unlink()
                except Product.DoesNotExist:
                    pass

            if self.video:
                try:
                    if current_product.video and current_product.video != self.video:
                        video_path = Path(current_product.video.path)
                        if video_path.exists():
                            video_path.unlink()
                except Product.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Video(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = 'order',

    video = models.FileField(upload_to=path_to_video, blank=False, verbose_name='Видео-файл')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, verbose_name='Продукт', related_name='videos')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')
