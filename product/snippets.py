from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class ProductTag(models.Model):
    url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=255)

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = "Menu san pham"
        verbose_name_plural = "Menu san pham"

    def __str__(self):
        return self.text
