# Generated by Django 4.2.11 on 2024-04-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htapp2', '0002_client_address_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photos/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
