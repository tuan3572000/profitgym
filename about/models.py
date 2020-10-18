from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from home import blocks


class AboutPage(Page):

    description = StreamField(
        [
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=False,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("description"),
    ]

    class Meta:
        verbose_name= "Gioi thieu"
