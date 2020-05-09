from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from home import blocks


class ContactPage(Page):

    description = StreamField(
        [
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=False,
        blank=True
    )
    location = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete= models.SET_NULL,
    )
    location_ggmap_url = models.URLField(blank=True, null=True)
    max_count = 1

    content_panels = Page.content_panels + [
        StreamFieldPanel("description"),
        ImageChooserPanel("location"),
        FieldPanel("location_ggmap_url")
    ]

    class Meta:
        verbose_name= "Thong tin lien he"
