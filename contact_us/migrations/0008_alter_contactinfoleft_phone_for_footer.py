# Generated by Django 4.1.7 on 2023-02-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0007_medialinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfoleft',
            name='phone_for_footer',
            field=models.CharField(max_length=30),
        ),
    ]
