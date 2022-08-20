from django import template


register = template.Library()


@register.filter
def my_filter(value, arg):
    # Implementation logic of the filter
    pass