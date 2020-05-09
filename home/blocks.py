from wagtail.core import blocks


class RichtextBlock(blocks.RichTextBlock):

    class Meta:
        template = "blocks/richtext_block.html",
        icon = "edit",
        label = "Full richtext"
