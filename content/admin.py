from django.contrib import admin
from django.utils.html import format_html, strip_tags

from content.models import Page, SocialNetwork, PaymentMethods, Contact, Vacancy, Review, Benefit, AboutHome, Slider


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'slug', 'place_1', 'place_2', 'place_3', 'place_4', 'order')
    list_display_links = ('title', )
    list_editable = ('place_1', 'place_2', 'place_3', 'place_4', 'order')
    list_filter = ('place_1', 'place_2', 'place_3', 'place_4')

    prepopulated_fields = {"slug": ('title',)}
    search_fields = ('title', 'text', 'slug', 'author')

    ordering = ('order', )

    fieldsets = (
        ('Основная информация', {
            'fields': (
                'title', 'text_1', 'image_1', 'text_2', 'image_2', 'text_3', 'image_3'
            )
        }),
        ('Дополнительно', {
            'fields': (
                'type', 'order', 'slug'
            )
        }),
        ('Показ в блоках', {
            'fields': ('place_1', 'place_2', 'place_3', 'place_4'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': (
                'keywords', 'description'
            ),
            'classes': ('collapse',)
        }),
    )


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_display_links = ('title', )
    list_editable = ('order',)


@admin.register(PaymentMethods)
class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_icon', 'order')
    list_display_links = ('title', 'get_icon')
    list_editable = ('order',)

    def get_icon(self, obj):
        return format_html('<img src="{}">', obj.icon.url)

    get_icon.short_description = 'Иконка'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_icon', 'get_text', 'order')
    list_display_links = ('title', 'get_icon')
    list_editable = ('order',)

    def get_icon(self, obj):
        return format_html('<img src="{}">', obj.icon.url)

    get_icon.short_description = 'Иконка'

    def get_text(self, obj):
        return obj.text if len(obj.text) < 32 else obj.text[:32] + '...'

    get_text.short_description = 'Текст'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_display_links = ('title',)
    list_editable = ('order',)

    search_fields = ('title', 'text')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_photo', 'get_review', 'get_photo_review', 'published_at')
    list_display_links = ('name',)

    search_fields = ('name', 'review')

    def get_photo(self, obj):
        if obj.photo_client:
            return format_html('<img src="{}" width="56" height="56" style="object-fit: contain;">', obj.photo_client.url)
        else:
            return '—'

    get_photo.short_description = 'Фото клиента'

    def get_photo_review(self, obj):
        if obj.photo_review:
            return format_html('<img src="{}" width="56" height="56" style="object-fit: contain;">',
                               obj.photo_review.url)
        else:
            return '—'

    get_photo_review.short_description = 'Фото отзыва'

    def get_review(self, obj):
        clean_text = strip_tags(obj.review)
        return clean_text[:32] + '...' if len(clean_text) > 32 else clean_text

    get_review.short_description = 'Отзыв'


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_display_links = ('title',)
    list_editable = ('order',)


@admin.register(AboutHome)
class AboutHomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')
    list_display_links = ('title', 'get_image')

    def get_image(self, obj):
        return format_html('<img src="{}" width="160" height="90" style="object-fit: cover;">', obj.image.url)

    get_image.short_description = 'Картинка'


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'order')
    list_display_links = ('title', 'get_image')
    list_editable = ('order',)

    def get_image(self, obj):
        return format_html('<img src="{}" width="160" height="90" style="object-fit: cover;">', obj.image.url)

    get_image.short_description = 'Картинка'
