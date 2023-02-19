import os
import uuid

from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.


class ServicesInfoOffer(models.Model):
    """
    Model for a service offer on the services page.

    Fields:
    - header: CharField with max length of 200 characters.
    - slug: SlugField with max length of 200 characters and db_index=True.
    - small_description: TextField with max length of 500 characters.
    - heading_text_left: HTMLField with max length of 1000 characters.
    - heading_text_right: HTMLField with max length of 1000 characters.
    - little_logo: PositiveSmallIntegerField with default value of 1, representing the service offer's logo:
        1 - House with tablet "NEW"
        2 - Regular house
        3 - Building
        4 - Agent in front of the house
        5 - House in the hand
        6 - Modern house
    - photo_1: ImageField with a function named `get_file_name` that determines the filename for the uploaded image.
    - photo_2: ImageField with a function named `get_file_name` that determines the filename for the uploaded image.
    - photo_3: ImageField with a function named `get_file_name` that determines the filename for the uploaded image.
    - font_image_for_service_page: ImageField with a function named `get_file_name` that determines the filename for the
        uploaded image. This field represents the image that will be shown on the background of the service offer.
    - is_visible: BooleanField with default value of True. Determines if the service offer is visible on the site.

    Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """

    def get_file_name(self, filename: str) -> str:
        """
        Method to rename the photo file with unique filename.

        Args:
            filename (str): Name of the file.

        Returns:
            str: Path to the photo with unique name.
        """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('services/', new_filename)

    header = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    small_description = models.TextField(max_length=500)
    heading_text_left = HTMLField(max_length=1000)
    heading_text_right = HTMLField(max_length=1000)
    little_logo = models.PositiveSmallIntegerField(default=1,
                                                   help_text='1 - House with tablet "NEW"\n, 2 - Regular house,'
                                                             ' 3 - Building, 4 - Agent in front of the house,'
                                                             ' 5 - House in the hand, 6 - Modern house.')
    photo_1 = models.ImageField(upload_to=get_file_name)
    photo_2 = models.ImageField(upload_to=get_file_name)
    photo_3 = models.ImageField(upload_to=get_file_name)
    font_image_for_service_page = models.ImageField(upload_to=get_file_name,
                                                    help_text='Image will show on the background of the service offer')
    is_visible = models.BooleanField(default=True, help_text='Is service visible on site.')

    def get_absolute_url(self):
        """
        Returns the absolute URL of the service offer.

        Returns:
            str: The absolute URL of the service offer.
        """
        return reverse("services:services_direct_view", args=[self.id, self.slug])

    class Meta:
        verbose_name = '1. Services Info'
        verbose_name_plural = '1. Services Info'
