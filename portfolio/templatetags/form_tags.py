from django import template
from django.forms.boundfield import BoundField

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    """
    Add a CSS class to a form field
    Usage: {{ form.field|add_class:"my-class" }}
    """
    if isinstance(value, BoundField):
        css_classes = value.field.widget.attrs.get('class', '')
        if css_classes:
            css_classes = f"{css_classes} {arg}"
        else:
            css_classes = arg
        return value.as_widget(attrs={'class': css_classes})
    return value
