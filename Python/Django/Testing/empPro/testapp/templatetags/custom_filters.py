# custom_filters.py

from django import template

register = template.Library()

@register.filter(name='add_dollar')
def add_dollar(value):
    return f"${value}"
