# Generated by Django 4.1.4 on 2023-03-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_delivery_options_alter_delivery_fee_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='address',
            field=models.TextField(default='10 Obe Street'),
            preserve_default=False,
        ),
    ]
