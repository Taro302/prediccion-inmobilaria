from django import template

register = template.Library()

@register.filter
def add_commas(value):
    return "{:,.2f}".format(value)
