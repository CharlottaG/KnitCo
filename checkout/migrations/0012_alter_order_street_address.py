# Generated by Django 5.0.6 on 2024-07-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_remove_order_street_address1_order_street_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address',
            field=models.CharField(max_length=80),
        ),
    ]