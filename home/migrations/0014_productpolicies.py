# Generated by Django 2.2.8 on 2020-07-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200713_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPolicies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/product')),
            ],
        ),
    ]
