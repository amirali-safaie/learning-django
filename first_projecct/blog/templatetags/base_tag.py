from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag("blog/partial/navbar_tag.html")
def category_navbar():
    return {"category":Category.objects.filter(status = True)}

@register.inclusion_tag("registration/partial/active_bar.html") #این تگ برای اکتیو باره لینک و اسم و اون تیکه رو میگیره و یک منو درست میکنه
def active_bar(request,link_name,content):
    return {
        "request":request,
        "link_name":link_name, #لینکی که میخوام بهش برم 
        "link":f'account:{link_name}',
        "content":content
    }


