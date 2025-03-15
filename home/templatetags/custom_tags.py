from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("home/include/product.html")
def show_product(img, price, name, pk):
    return {
        "img": img,
        "price": "$" + str(price),
        "name": name,
        "MEDIA_URL": settings.MEDIA_URL,
        "pk": pk,
    }
