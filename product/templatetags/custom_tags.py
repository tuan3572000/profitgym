from django import template

from contact.snippets import ContactTag
from product.snippets import ProductTag

register = template.Library()

@register.inclusion_tag('product/product_tags.html', takes_context=True)
def product_tags(context):
    return {
        'product_tags': ProductTag.objects.all(),
        'request': context['request'],
    }


@register.inclusion_tag('contact/contact_tags.html', takes_context=True)
def contact_tags(context):
    return {
        'contact_tags': ContactTag.objects.all(),
        'request': context['request'],
    }