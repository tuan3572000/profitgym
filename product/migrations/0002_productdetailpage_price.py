# Generated by Django 3.0.6 on 2020-05-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetailpage',
            name='price',
            field=models.CharField(help_text='Gia ban', max_length=100, null=True),
        ),
    ]