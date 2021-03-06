# Generated by Django 3.0.6 on 2020-06-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200513_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('parent_url', models.URLField(blank=True, null=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
    ]
