from django import template

register = template.Library()


@register.filter
def identifier(value):
    if not value:
        return ""
    return value.split(" ", 1)[0]
