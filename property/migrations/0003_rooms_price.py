# Generated by Django 4.1.5 on 2023-01-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_rename_properties_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='price',
            field=models.PositiveIntegerField(default=1, verbose_name='Price per night'),
            preserve_default=False,
        ),
    ]
