"""This file is used for custom template filters for basic_app"""
from django import template

# NOTE: Templates must be registered
register = template.Library()


# NOTE: filters can be registered with decorators
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')
