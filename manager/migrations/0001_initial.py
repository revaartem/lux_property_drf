# Generated by Django 4.1.7 on 2023-02-17 14:15

from django.db import migrations, models
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundImagesForPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_menu_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('about_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('contact_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('services_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('manager_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('archive_manager_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
                ('unprocessed_applications_bg', models.ImageField(upload_to=manager.models.BackgroundImagesForPages.get_file_name)),
            ],
        ),
    ]