# Generated by Django 5.0.6 on 2024-07-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
