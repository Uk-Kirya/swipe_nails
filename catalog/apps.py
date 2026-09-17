from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Каталог'

    def ready(self):
        import swipe_nails.signals
