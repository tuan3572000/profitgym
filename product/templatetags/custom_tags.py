from django import template

from about.snippets import AboutTag
from contact.snippets import ContactTag
from home.snippets import WelcomeTag, MenuTag
from product.snippets import ProductTag

register = template.Library()

# @register.inclusion_tag('product/product_tags.html', takes_context=True)
# def product_tags(context):
#     return {
#         'product_tags': ProductTag.objects.all(),
#         'request': context['request'],
#     }


@register.inclusion_tag('contact/contact_tags.html', takes_context=True)
def contact_tags(context):
    return {
        'contact_tags': ContactTag.objects.all(),
        'request': context['request'],
    }

@register.inclusion_tag('home/welcome_tags.html', takes_context=True)
def welcome_tags(context):
    return {
        'welcome_tags': WelcomeTag.objects.all(),
        'request': context['request'],
    }

@register.inclusion_tag('home/menu_tags.html', takes_context=True)
def menu_tags(context):
    return {
        'menu_tags': MenuTag.objects.all(),
        'request': context['request'],
    }

@register.inclusion_tag('about/about_tags.html', takes_context=True)
def about_tags(context):
    return {
        'about_tags': AboutTag.objects.all(),
        'request': context['request'],
    }