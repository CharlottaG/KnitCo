# Generated by Django 5.0.6 on 2024-06-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
