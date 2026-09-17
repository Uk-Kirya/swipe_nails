from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'content'
    verbose_name = 'Контент сайта'

    def ready(self):
        import swipe_nails.signals
