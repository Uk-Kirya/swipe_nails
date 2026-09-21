import os
from uuid import uuid4
from pathlib import Path

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


def path_to_pages_images(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join('pages', filename)


def path_to_slider_images(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join('slider', filename)


def path_to_about_images(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join('about', filename)


def path_to_review_photos(instance, filename):
    filename = f"{uuid4()}.webp"
    return os.path.join('reviews', filename)


def path_to_icons_payment_methods(instance, filename):
    if filename.endswith('.svg'):
        return os.path.join('payment_methods', filename)
    else:
        filename = f"{uuid4()}.webp"
        return os.path.join('payment_methods', filename)


def path_to_icons_contacts(instance, filename):
    if filename.endswith('.svg'):
        return os.path.join('contacts', filename)
    else:
        filename = f"{uuid4()}.webp"
        return os.path.join('contacts', filename)


def path_to_icons_benefits(instance, filename):
    if filename.endswith('.svg'):
        return os.path.join('benefits', filename)
    else:
        filename = f"{uuid4()}.webp"
        return os.path.join('benefits', filename)


class Page(models.Model):
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = 'order',

    TYPE = [
        ('text', 'Текстовая'),
        ('catalog', 'Каталог'),
        ('about', 'О компании'),
        ('reviews', 'Отзывы'),
        ('contacts', 'Контакты'),
        ('career', 'Карьера'),
        ('faq', 'FAQ'),
        ('instructions', 'Инструкции'),
        ('materials', 'Материалы'),
    ]

    title = models.CharField(max_length=500, blank=False, verbose_name='Заголовок')
    type = models.CharField(max_length=100, default='text', choices=TYPE, verbose_name='Шаблон')

    text_1 = RichTextUploadingField(blank=True, verbose_name='Текст 1')
    image_1 = models.ImageField(upload_to=path_to_pages_images, blank=True, verbose_name='Картинка 1')
    text_2 = RichTextUploadingField(blank=True, verbose_name='Текст 2')
    image_2 = models.ImageField(upload_to=path_to_pages_images, blank=True, verbose_name='Картинка 2')
    text_3 = RichTextUploadingField(blank=True, verbose_name='Текст 3')
    image_3 = models.ImageField(upload_to=path_to_pages_images, blank=True, verbose_name='Картинка 3')

    keywords = models.TextField(blank=True, verbose_name='Keywords')
    description = models.TextField(blank=True, verbose_name='Description')

    is_active = models.BooleanField(default=True, verbose_name='Активная?')
    is_dedicated = models.BooleanField(default=False, verbose_name='Выделенный пункт?')
    header_menu = models.BooleanField(default=False, verbose_name='Отображать в основном меню?')
    footer_menu = models.BooleanField(default=False, verbose_name='Отображать в подвале?')
    order = models.IntegerField(default=0, blank=True, verbose_name='Порядок')
    slug = models.SlugField(max_length=255, blank=True, verbose_name='Slug')

    place_1 = models.BooleanField(default=False, verbose_name='Header')
    place_2 = models.BooleanField(default=False, verbose_name='Footer 1')
    place_3 = models.BooleanField(default=False, verbose_name='Footer 2')
    place_4 = models.BooleanField(default=False, verbose_name='Footer 3')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.pk:
            current_page = Page.objects.get(pk=self.pk)

            if self.image_1:
                try:
                    if current_page.image_1 and current_page.image_1 != self.image_1:
                        image_path = Path(current_page.image_1.path)
                        if image_path.exists():
                            image_path.unlink()
                except Page.DoesNotExist:
                    pass

            if self.image_2:
                try:
                    if current_page.image_2 and current_page.image_2 != self.image_2:
                        image_path = Path(current_page.image_2.path)
                        if image_path.exists():
                            image_path.unlink()
                except Page.DoesNotExist:
                    pass

            if self.image_3:
                try:
                    if current_page.image_3 and current_page.image_3 != self.image_3:
                        image_path = Path(current_page.image_3.path)
                        if image_path.exists():
                            image_path.unlink()
                except Page.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class SocialNetwork(models.Model):
    class Meta:
        verbose_name = 'Соц.сеть'
        verbose_name_plural = 'Соц.сети'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    link = models.CharField(max_length=500, blank=False, verbose_name='Ссылка')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')


class PaymentMethods(models.Model):
    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    icon = models.FileField(upload_to=path_to_icons_payment_methods, blank=False, verbose_name='Иконка')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')

    def save(self, *args, **kwargs):
        if self.pk:
            current_payment = PaymentMethods.objects.get(pk=self.pk)

            if self.icon:
                try:
                    if current_payment.icon and current_payment.icon != self.icon:
                        icon_path = Path(current_payment.icon.path)
                        if icon_path.exists():
                            icon_path.unlink()
                except PaymentMethods.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    icon = models.FileField(upload_to=path_to_icons_contacts, blank=False, verbose_name='Иконка')
    text = models.CharField(max_length=500, blank=False, verbose_name='Текст')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')

    def save(self, *args, **kwargs):
        if self.pk:
            current_contact = Contact.objects.get(pk=self.pk)

            if self.icon:
                try:
                    if current_contact.icon and current_contact.icon != self.icon:
                        icon_path = Path(current_contact.icon.path)
                        if icon_path.exists():
                            icon_path.unlink()
                except Contact.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Vacancy(models.Model):
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    text = RichTextUploadingField(blank=False, verbose_name='Текст')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')


class Review(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = '-published_at',

    name = models.CharField(max_length=255, blank=False, verbose_name='Имя')
    photo_client = models.ImageField(upload_to=path_to_review_photos, blank=False, verbose_name='Фото клиента')
    review = RichTextUploadingField(blank=False, verbose_name='Текст отзыва')
    photo_review = models.ImageField(upload_to=path_to_review_photos, blank=False, verbose_name='Фото отзыва')
    published_at = models.DateTimeField(auto_now=True, blank=False, verbose_name='Дата публикации')

    def save(self, *args, **kwargs):
        if self.pk:
            current_review = Review.objects.get(pk=self.pk)

            if self.photo_client:
                try:
                    if current_review.photo_client and current_review.photo_client != self.photo_client:
                        photo_client_path = Path(current_review.photo_client.path)
                        if photo_client_path.exists():
                            photo_client_path.unlink()
                except Review.DoesNotExist:
                    pass

            if self.photo_review:
                try:
                    if current_review.photo_review and current_review.photo_review != self.photo_review:
                        photo_review_path = Path(current_review.photo_review.path)
                        if photo_review_path.exists():
                            photo_review_path.unlink()
                except Review.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Benefit(models.Model):
    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    icon = models.FileField(upload_to=path_to_icons_benefits, blank=False, verbose_name='Иконка')
    animation = models.IntegerField(default=0, blank=True, verbose_name='Задержка появления (м.сек)')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')

    def save(self, *args, **kwargs):
        if self.pk:
            current_benefit = Benefit.objects.get(pk=self.pk)

            if self.icon:
                try:
                    if current_benefit.icon and current_benefit.icon != self.icon:
                        icon_path = Path(current_benefit.icon.path)
                        if icon_path.exists():
                            icon_path.unlink()
                except Benefit.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class AboutHome(models.Model):
    class Meta:
        verbose_name = 'О компании на главной'
        verbose_name_plural = 'О компании на главной'

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    image = models.ImageField(upload_to=path_to_about_images, blank=False, verbose_name='Картинка')
    text = models.TextField(blank=False, verbose_name='Текст')

    def save(self, *args, **kwargs):
        if self.pk:
            current_about_home = AboutHome.objects.get(pk=self.pk)

            if self.image:
                try:
                    if current_about_home.image and current_about_home.image != self.image:
                        current_about_home_path = Path(current_about_home.image.path)
                        if current_about_home_path.exists():
                            current_about_home_path.unlink()
                except AboutHome.DoesNotExist:
                    pass

        super().save(*args, **kwargs)


class Slider(models.Model):
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайдер'
        ordering = 'order',

    title = models.CharField(max_length=255, blank=False, verbose_name='Заголовок')
    image = models.ImageField(upload_to=path_to_slider_images, blank=False, verbose_name='Картинка')
    text = models.TextField(blank=False, verbose_name='Текст')
    text_on_button = models.CharField(max_length=255, blank=False, verbose_name='Текст на кнопке')
    link_on_button = models.CharField(max_length=500, blank=False, verbose_name='Ссылка на кнопке')
    order = models.IntegerField(default=0, blank=False, verbose_name='Порядковый номер')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            current_slide = Slider.objects.get(pk=self.pk)

            if self.image:
                try:
                    if current_slide.image and current_slide.image != self.image:
                        current_slide_path = Path(current_slide.image.path)
                        if current_slide_path.exists():
                            current_slide_path.unlink()
                except Slider.DoesNotExist:
                    pass

        super().save(*args, **kwargs)
