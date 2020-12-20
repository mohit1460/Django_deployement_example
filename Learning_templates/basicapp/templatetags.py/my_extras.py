from django import template

register=template.Library()

@register.filter()
def cut(arg):
    return arg.replace(arg,'')

#register.filter(cut)
