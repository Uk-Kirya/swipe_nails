from django.contrib import admin
from django.utils.html import format_html, strip_tags

from .models import InstructionCard, QuestionInstruction, ExpertAdvice


@admin.register(InstructionCard)
class InstructionCardAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'order')
    search_fields = ('text',)

    def get_image(self, obj):
        return format_html('<img src="{}" width="128" height="128" style="object-fit: cover;">', obj.image.url)

    get_image.short_description = 'Картинка'


@admin.register(QuestionInstruction)
class QuestionInstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('text',)


@admin.register(ExpertAdvice)
class ExpertAdviceAdmin(admin.ModelAdmin):
    list_display = ('get_text', 'block', 'order')
    search_fields = ('text',)
    list_filter = ('block',)

    def get_text(self, obj):
        clean_text = strip_tags(obj.text)
        return clean_text[:56] + ' ...' if len(clean_text) > 56 else clean_text

    get_text.short_description = 'Текст'
