from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core.blocks import CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel

from home import blocks


class ProductListingPage(Page):

    """Listing product pages"""

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context["products"] = ProductDetailPage.objects.live().public()
    #     return context
    description = StreamField(
        [
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=False,
        blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel("description")
    ]


    class Meta:
        verbose_name = "Loai san pham"


class ProductDetailPage(Page):

    """ Detail of product """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Ten san pham'
    )

    inStock = models.BooleanField(
        null=True,
        blank=False,
        default=True,
        help_text = 'Con hang ?'
    )

    weight = models.CharField(
        max_length=10,
        blank=False,
        null=True,
        help_text='Trong luong'
    )

    brief = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text='Mo ta ngan gon'
    )

    price = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Gia ban'
    )

    images = StreamField([
        ('image', ImageChooserBlock()),
    ],
    null= True)


    description = StreamField(
        [   ('title_block', CharBlock()),
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("price"),
        FieldPanel("weight"),
        FieldPanel("inStock"),
        StreamFieldPanel("images"),
        FieldPanel("brief"),
        StreamFieldPanel("description")
    ]

    class Meta:
        verbose_name = "Chi tiet san pham"
