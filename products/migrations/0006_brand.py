# Generated by Django 5.0.6 on 2024-06-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('location', models.CharField(max_length=254, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
