from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from home import blocks


class ProductListingPage(Page):

    """Listing product pages"""

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["products"] = ProductDetailPage.objects.live().public()
        return context

    class Meta:
        verbose_name = "Loai san pham"


class ProductDetailPage(Page):

    """ Detail of product """
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Product name'
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete= models.SET_NULL,
    )

    description = StreamField(
        [
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=False,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        ImageChooserPanel("image"),
        StreamFieldPanel("description")
    ]

    class Meta:
        verbose_name = "Chi tiet san pham"
