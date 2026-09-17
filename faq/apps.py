from django.apps import AppConfig


class FaqConfig(AppConfig):
    name = 'faq'
    verbose_name = 'FAQ'

    def ready(self):
        import swipe_nails.signals
