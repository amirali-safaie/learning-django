from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("htmls_file/partial/navbar_tag.html")
def category_navbar():
    return {"category":Category.objects.filter(status = True)}

