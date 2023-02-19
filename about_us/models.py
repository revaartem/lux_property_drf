import os
import uuid

from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class AboutUsTopInfo(models.Model):
    """
    Model to store the text for the top info block on the About Us page.

    Fields:
    - left_heading_text: the text to display on the left side of the top info block (HTMLField, max length 800).
    - right_heading_text: the text to display on the right side of the top info block (HTMLField, max length 800).
    """

    left_heading_text = HTMLField(max_length=800)
    right_heading_text = HTMLField(max_length=800)

    def __str__(self):
        """
        Returns the first 50 characters of the left_heading_text, or the full left_heading_text if it is less than
        50 characters.
        """

        if len(self.left_heading_text) > 50:
            return f'{self.left_heading_text[:50]}'
        else:
            return f'{self.left_heading_text}'

    class Meta:
        """
        Metadata for the AboutUsTopInfo model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        verbose_name = '1. Top info block'
        verbose_name_plural = '1. Top info block'


class FirstBenefitsBlock(models.Model):
    """
    Model to store the text and image for the first benefits block on the About Us page.

    Fields:
    - house_point_header: the header text for the first benefit (TextField, max length 500).
    - house_point_heading_text: the body text for the first benefit (TextField, max length 500).
    - agents_point_header: the header text for the second benefit (TextField, max length 500).
    - agents_point_heading_text: the body text for the second benefit (TextField, max length 500).
    - safety_point_header: the header text for the third benefit (TextField, max length 500).
    - safety_point_heading_text: the body text for the third benefit (TextField, max length 500).
    - image: the image to display for the first benefits block (ImageField).
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
        return os.path.join('about_us/first_benefits_block/', new_filename)

    house_point_header = models.TextField(max_length=500)
    house_point_heading_text = models.TextField(max_length=500)
    agents_point_header = models.TextField(max_length=500)
    agents_point_heading_text = models.TextField(max_length=500)
    safety_point_header = models.TextField(max_length=500)
    safety_point_heading_text = models.TextField(max_length=500)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        """
        Returns a string that identifies the block by its primary key.
        """

        return f'Block {self.pk}'

    class Meta:
        """
        Metadata for the FirstBenefitsBlock model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        verbose_name = '2. First benefits block'
        verbose_name_plural = '2. First benefit block'


class SecondBenefitsBlock(models.Model):
    """
    A model to represent the second benefits block in the About Us page.

    Attributes:
        house_point_header (str): A string representing the header of the house point section.
        house_point_heading_text (str): A string representing the heading text of the house point section.
        agents_point_header (str): A string representing the header of the agents point section.
        agents_point_heading_text (str): A string representing the heading text of the agents point section.
        safety_point_header (str): A string representing the header of the safety point section.
        safety_point_heading_text (str): A string representing the heading text of the safety point section.
        image (ImageField): An image representing the second benefits block.

    Methods:
        get_file_name: A method that returns a new filename for an image to be uploaded to this model's ImageField.

    Meta:
        verbose_name (str): A string representing the singular name of this model in the admin interface.
        verbose_name_plural (str): A string representing the plural name of this model in the admin interface.
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
        return os.path.join('about_us/second_benefits_block/', new_filename)

    house_point_header = models.TextField(max_length=500)
    house_point_heading_text = models.TextField(max_length=500)
    agents_point_header = models.TextField(max_length=500)
    agents_point_heading_text = models.TextField(max_length=500)
    safety_point_header = models.TextField(max_length=500)
    safety_point_heading_text = models.TextField(max_length=500)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        """
        Returns a string that identifies the block by its primary key.
        """

        return f'Block {self.pk}'

    class Meta:
        """
        Metadata for the SecondBenefitsBlock model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        verbose_name = '3. Second benefits block'
        verbose_name_plural = '3. Second benefits block'


class PhotosAndNumbers(models.Model):
    """
    A model to represent the photos and numbers block in the About Us page.

    Attributes:
        image_1 (ImageField): An image for the first section of the photos and numbers block.
        image_2 (ImageField): An image for the second section of the photos and numbers block.
        image_3 (ImageField): An image for the third section of the photos and numbers block.
        block_1_header_number (str): A string representing the number of the first section of the block.
        block_1_heading_text (str): A string representing the heading text of the first section of the block.
        block_2_header_number (str): A string representing the number of the second section of the block.
        block_2_heading_text (str): A string representing the heading text of the second section of the block.
        block_3_header_number (str): A string representing the number of the third section of the block.
        block_3_heading_text (str): A string representing the heading text of the third section of the block.
        block_4_header_number (str): A string representing the number of the fourth section of the block.
        block_4_heading_text (str): A string representing the heading text of the fourth section of the block.

    Methods:
        get_file_name: A method that returns a new filename for an image to be uploaded to this model's ImageField.

    Meta:
        verbose_name (str): A string representing the singular name of this model in the admin interface.
        verbose_name_plural (str): A string representing the plural name of this model in the admin interface.
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
        return os.path.join('about_us/photos_and_numbers/', new_filename)

    image_1 = models.ImageField(upload_to=get_file_name)
    image_2 = models.ImageField(upload_to=get_file_name)
    image_3 = models.ImageField(upload_to=get_file_name)
    block_1_header_number = models.CharField(max_length=10)
    block_1_heading_text = models.CharField(max_length=100)
    block_2_header_number = models.CharField(max_length=10)
    block_2_heading_text = models.CharField(max_length=100)
    block_3_header_number = models.CharField(max_length=10)
    block_3_heading_text = models.CharField(max_length=100)
    block_4_header_number = models.CharField(max_length=10)
    block_4_heading_text = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string that identifies the block by its primary key.
        """

        return f'Block {self.pk}'

    class Meta:
        """
        Metadata for the PhotosAndNumbers model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        verbose_name = '4. Photos and numbers block'
        verbose_name_plural = '4. Photos and numbers block'


class TeamMember(models.Model):
    """
    Model to represent a team member.

    Attributes:
        photo (django.db.models.ImageField): An image field for the team member's photo.
        name (django.db.models.CharField): A char field for the team member's name (max length: 40).
        position (django.db.models.CharField): A char field for the team member's position (max length: 25).
        short_about (django.db.models.CharField): A char field for a short description of the team member
        (max length: 120).
        instagram_link (django.db.models.CharField): A char field for the team member's Instagram link
        (max length: 500).
        twitter_link (django.db.models.CharField): A char field for the team member's Twitter link (max length: 500).
        facebook_link (django.db.models.CharField): A char field for the team member's Facebook link (max length: 500).
        linkedin_link (django.db.models.CharField): A char field for the team member's LinkedIn link (max length: 500).
        visible_in_our_agents (django.db.models.BooleanField): A boolean field to indicate whether the team member is
        visible in our agents page (default: True).
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
        return os.path.join('about_us/team_members/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    name = models.CharField(max_length=40)
    position = models.CharField(max_length=25)
    short_about = models.CharField(max_length=120, help_text='Short description, less than 120 chars.')
    instagram_link = models.CharField(blank=True, max_length=500)
    twitter_link = models.CharField(blank=True, max_length=500)
    facebook_link = models.CharField(blank=True, max_length=500)
    linkedin_link = models.CharField(blank=True, max_length=500)
    visible_in_our_agents = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns the string representation of the team member.

        Returns:
            str: The name of the team member.
        """

        return f'{self.name}'

    class Meta:
        """
        Metadata for the TeamMember model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        verbose_name = '5. Team member'
        verbose_name_plural = '5. Team members'
