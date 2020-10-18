# Generated by Django 3.0.6 on 2020-05-09 17:31

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Loai san pham',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Menu san pham',
                'verbose_name_plural': 'Menu san pham',
            },
        ),
        migrations.CreateModel(
            name='ProductDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(help_text='Product name', max_length=100)),
                ('description', wagtail.core.fields.StreamField([('richtext_block', home.blocks.RichtextBlock())], blank=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Chi tiet san pham',
            },
            bases=('wagtailcore.page',),
        ),
    ]