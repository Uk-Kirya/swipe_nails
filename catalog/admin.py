from django.contrib import admin
from django.utils.html import format_html
from catalog.models import Category, Style, Color, Product, AccessoriesCategory, Video


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_cover', 'get_icon', 'order')
    list_display_links = ('title', 'get_cover', 'get_icon')
    list_editable = ('order',)

    prepopulated_fields = {"slug": ('title',)}
    search_fields = ('title', 'text')

    ordering = ('order',)

    def get_cover(self, obj):
        return format_html('<img src="{}" width="160" height="90" style="object-fit: cover;">', obj.cover.url)

    get_cover.short_description = 'Обложка'

    def get_icon(self, obj):
        return format_html('<img src="{}" width="48" height="48" style="object-fit: contain;">', obj.icon.url)

    get_icon.short_description = 'Иконка'


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_cover', 'order')
    list_display_links = ('title', 'get_cover')
    list_editable = ('order',)

    prepopulated_fields = {"slug": ('title',)}
    search_fields = ('title', 'text')

    ordering = ('order',)

    def get_cover(self, obj):
        return format_html('<img src="{}" width="160" height="90" style="object-fit: cover;">', obj.cover.url)

    get_cover.short_description = 'Обложка'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    ordering = ('title',)


@admin.register(AccessoriesCategory)
class AccessoriesCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_cover', 'order')
    list_display_links = ('title', 'get_cover')
    list_editable = ('order',)

    prepopulated_fields = {"slug": ('title',)}
    search_fields = ('title', 'text')

    ordering = ('order',)

    def get_cover(self, obj):
        return format_html('<img src="{}" width="160" height="90" style="object-fit: cover;">', obj.cover.url)

    get_cover.short_description = 'Обложка'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'get_cover_1',
        'get_cover_2',
        'category',
        'style',
        'color',
        'acessories',
        'in_stock',
        'popular',
        'new',
        'order'
    )
    list_display_links = ('title', 'get_cover_1', 'get_cover_2')
    list_editable = ('price', 'category', 'style', 'color', 'acessories', 'in_stock', 'popular', 'new', 'order')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'text_1', 'text_2', 'text_3', 'text_4', 'text_5')
    list_filter = ('category', 'style', 'color', 'acessories', 'in_stock', 'new')
    ordering = ('order',)

    fieldsets = (
        (
            'Основная информация',
            {
                'fields': (
                    'title',
                    'price',
                    'type',
                ),
            },
        ),
        (
            'Изображения и видео',
            {
                'fields': (
                    'cover_1',
                    'cover_2',
                    'video',
                ),
            },
        ),
        (
            'Категоризация',
            {
                'fields': (
                    'category',
                    'style',
                    'color',
                    'acessories',
                ),
            },
        ),
        (
            'Тексты',
            {
                'fields': (
                    'text_1',
                    'text_2',
                    'text_3',
                    'text_4',
                    'text_5',
                ),
            },
        ),
        (
            'Статус и сортировка',
            {
                'fields': (
                    'in_stock',
                    'popular',
                    'new',
                    'order',
                ),
            },
        ),
        (
            'SEO',
            {
                'fields': (
                    'slug',
                    'keywords',
                    'description',
                ),
            },
        ),
    )

    def get_cover_1(self, obj):
        return format_html('<img src="{}" width="30" height="40" style="object-fit: cover;">', obj.cover_1.url)

    get_cover_1.short_description = 'Обложка 1'

    def get_cover_2(self, obj):
        return format_html('<img src="{}" width="30" height="40" style="object-fit: cover;">', obj.cover_2.url)

    get_cover_2.short_description = 'Обложка 2'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('product',)
    list_display_links = ('product',)
    ordering = ('order',)
