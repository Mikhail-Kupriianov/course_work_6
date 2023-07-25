from django import template

register = template.Library()


@register.filter()
def media_path(val):
    if val:
        return "/media/images/" + val

    return '#'


@register.simple_tag
def media_path(file_name):
    return "/media/images/"+file_name
