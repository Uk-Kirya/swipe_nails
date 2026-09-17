from django import template

register = template.Library()


@register.filter(name='price')
def price(value):
    try:
        return f"{int(value):,}".replace(",", " ")
    except (ValueError, TypeError):
        return value
