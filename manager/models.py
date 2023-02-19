import os
import uuid

from django.db import models

# Create your models here.


class BackgroundImagesForPages(models.Model):
    """
    Model to store background images for different pages on the website.

    Attributes:
        property_menu_bg (models.ImageField): Image for the property menu page background.
        about_bg (models.ImageField): Image for the about page background.
        contact_bg (models.ImageField): Image for the contact page background.
        services_bg (models.ImageField): Image for the services page background.
        manager_bg (models.ImageField): Image for the manager page background.
        archive_manager_bg (models.ImageField): Image for the archive manager page background.
        unprocessed_applications_bg (models.ImageField): Image for the unprocessed applications page background.

    Methods:
        get_file_name(filename: str) -> str: Method to generate a unique filename for the uploaded image.

    Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """

    def get_file_name(self, filename: str) -> str:
        """
        Generates a unique filename for the uploaded image.

        Args:
            filename (str): The original filename of the uploaded image.

        Returns:
            str: The new filename with a unique identifier and original file extension.

        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('backgrounds/', new_filename)

    property_menu_bg = models.ImageField(upload_to=get_file_name)
    about_bg = models.ImageField(upload_to=get_file_name)
    contact_bg = models.ImageField(upload_to=get_file_name)
    services_bg = models.ImageField(upload_to=get_file_name)
    manager_bg = models.ImageField(upload_to=get_file_name)
    archive_manager_bg = models.ImageField(upload_to=get_file_name)
    unprocessed_applications_bg = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
        - A string containing the words "Block of photos" followed by the primary key of the object.
        """
        return f'Block of photos {self.pk}'

    class Meta:
        verbose_name = '1. Background images for pages'
        verbose_name_plural = '1. Background images for pages'

