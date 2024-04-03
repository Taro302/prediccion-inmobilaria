from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter
def format_number(value):
    return floatformat(value, 0).replace(',', '.')

