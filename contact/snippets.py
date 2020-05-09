from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class ContactTag(models.Model):
    url = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel('url'),
    ]

    class Meta:
        verbose_name = "Menu lien he"
        verbose_name_plural = "Menu lien he"

    def __str__(self):
        return self.url
