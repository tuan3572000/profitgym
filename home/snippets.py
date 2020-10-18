from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from home import blocks


@register_snippet
class WelcomeTag(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text='Product name'
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    description = StreamField(
        [
            ('richtext_block', blocks.RichtextBlock()),
        ],
        null=True,
        blank=False
    )

    panels = [
        FieldPanel("name"),
        ImageChooserPanel('image'),
        StreamFieldPanel("description")
    ]

    class Meta:
        verbose_name = "Trang chu"
        verbose_name_plural = "Trang chu"

    def __str__(self):
        return self.name


@register_snippet
class MenuTag(models.Model):
    url = models.URLField(blank=False, null=True)
    name = models.CharField(max_length=255, blank=False)
    parent_url = models.URLField(blank=True, null=True)
    position = models.IntegerField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        FieldPanel('position'),
        FieldPanel('parent_url'),
    ]

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name + '('+ self.url+')'

