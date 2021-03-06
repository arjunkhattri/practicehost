# Generated by Django 2.2.8 on 2020-08-08 03:41

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200808_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPolicies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media/product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPoliciesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('ImageCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ProductPolicies')),
            ],
        ),
    ]
