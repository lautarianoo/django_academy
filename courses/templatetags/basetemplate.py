from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def basetemplate():
    categories = Category.objects.all()
    return {'categories': categories}
