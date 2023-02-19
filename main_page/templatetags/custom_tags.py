from django import template

register = template.Library()


@register.filter
def item_photo(photos, photo_owner):
    return photos.filter(property_item=photo_owner)


@register.filter('startswith')
def startswith(text, starts):
    if isinstance(text, str):
        return text.startswith(starts)
    return False
