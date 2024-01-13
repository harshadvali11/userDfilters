from django import template

register=template.Library()


@register.filter('swapping')
def swap(value):
    return value.swapcase()


@register.filter()
def remove(value,arg):
    return value.replace(arg,'')

@register.filter()
def counting(value,arg):
    c=0
    for ip in range(len(value)):
        if arg==value[ip:len(arg)+ip:1]:
            c+=1
    return c
'''
register.filter('counting',counting)
register.filter('swapping',swap)
register.filter('remove',remove)'''





