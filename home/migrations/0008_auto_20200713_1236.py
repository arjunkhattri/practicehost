# Generated by Django 2.2.8 on 2020-07-13 06:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200712_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognews',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
