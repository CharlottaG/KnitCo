# Generated by Django 5.0.6 on 2024-06-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]