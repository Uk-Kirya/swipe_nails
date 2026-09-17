from django.contrib import admin
from django.utils.html import format_html

from faq.models import CategoryFaq, QuestionFaq


@admin.register(CategoryFaq)
class FaqCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_icon', 'order')
    list_display_links = ('title', 'get_icon')
    list_editable = ('order',)

    def get_icon(self, obj):
        return format_html('<img src="{}" height="48" width="48" style="object-fit: cover;">',
                           obj.icon.url)

    get_icon.short_description = 'Иконка'


@admin.register(QuestionFaq)
class QuestionFaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_faq', 'order')
    list_display_links = ('title',)
    list_editable = ('order',)
    list_filter = ('category_faq',)

    search_fields = ('title', 'text')

