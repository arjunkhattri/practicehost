# Generated by Django 2.2.8 on 2020-07-11 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_galleryimage_galleryposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/gallery_posts/'),
        ),
    ]
