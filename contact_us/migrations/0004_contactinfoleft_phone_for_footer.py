# Generated by Django 4.1.7 on 2023-02-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0003_alter_contactinfoleft_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfoleft',
            name='phone_for_footer',
            field=models.IntegerField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]