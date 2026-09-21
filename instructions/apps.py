from django.apps import AppConfig


class InstructionsConfig(AppConfig):
    name = 'instructions'
    verbose_name = 'Блок с инструкциями'

    def ready(self):
        import swipe_nails.signals
