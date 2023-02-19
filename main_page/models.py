import os
import uuid

from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


# Create your models here.


class HeroHeader(models.Model):
    """
    Model for setting the header text on the website's main page.

    Attributes:
        text (str): The header text, formatted in HTML.

    Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """

    text = HTMLField(max_length=500, blank=True)

    def __str__(self):
        """
        Return a string representation of the HeroHeader instance.

        If the text is longer than 50 characters, return the first 50 characters followed by "...".
        Otherwise, return the entire text.

        Returns:
            str: A string representation of the HeroHeader instance.
        """
        if len(self.text) > 50:
            return f'{self.text[:50]}'
        else:
            return {self.text}

    class Meta:
        verbose_name = '1. Hero header'
        verbose_name_plural = '1. Hero header'


class HeroBackgroundPhotos(models.Model):
    """
    Model for the hero background photos that are displayed on the main page of the site.

    Fields:
    - photo: an image file that serves as the hero background photo.
    - is_visible: a boolean field indicating whether this photo should be displayed on the main page.

    Methods:
    - __str__: returns a string representation of the object, which is the string "Photo" followed by the primary
     key of the object.

     Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """

    def get_file_name(self, filename: str) -> str:
        """
        Returns a new filename for the uploaded photo that includes a unique identifier.

        Args:
        - filename: a string containing the name of the uploaded file.

        Returns:
        - A string containing the new filename, which includes a unique identifier.
        """

        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('hero/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        """
       Returns a string representation of the object.

       Returns:
       - A string containing the word "Photo" followed by the primary key of the object.
       """

        return f'Photo {self.pk}'

    class Meta:
        verbose_name = '2. Hero background photos'
        verbose_name_plural = '2. Hero background photos'


class Realtor(models.Model):
    """
    Model representing a realtor.

    Attributes:
        photo (ImageField): Image of the realtor.
        name (CharField): Name of the realtor.
        position (CharField): Position of the realtor.
        short_about (CharField): Short description of the realtor.
        instagram_link (CharField, optional): Link to the realtor's Instagram profile.
        twitter_link (CharField, optional): Link to the realtor's Twitter profile.
        facebook_link (CharField, optional): Link to the realtor's Facebook profile.
        linkedin_link (CharField, optional): Link to the realtor's LinkedIn profile.
        visible_in_our_agents (BooleanField): Whether the realtor is visible in the "Our Agents" section.

    Methods:
        get_file_name(filename: str) -> str: Returns a unique filename for the realtor's photo.

    Meta:
        verbose_name (str): A human-readable name for the model in singular form.
        verbose_name_plural (str): A human-readable name for the model in plural form.
    """

    def get_file_name(self, filename: str) -> str:
        """
        Returns a unique filename for the realtor's photo.

        """

        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('realtors/', new_filename)

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
        Returns the name of the realtor.

        """

        return f'{self.name}'

    class Meta:
        verbose_name = '6. Our agents'
        verbose_name_plural = '6. Our agents'


class Property(models.Model):
    """
        Model for a property, that can be displayed on the site.

    Attributes:
        name (str): The name of the property. Limited to 200 characters and must be unique.
        slug (str): A slug field that is used in URLs. Limited to 200 characters and indexed in the database.
        location_address (str): The address of the property. Limited to 300 characters.
        country (str): The country where the property is located. Limited to 50 characters.
        price (str): The price of the property in US dollars. Limited to 15 characters. Default is 0.
        description (HTMLField): A field for HTML-formatted text describing the property. Limited to 1000 characters.
        bed_quantity (int): The number of bedrooms in the property. Optional field.
        baths_quantity (int): The number of bathrooms in the property. Optional field.
        realtor (ForeignKey): A foreign key to the Realtor who is managing the property. This field is required.
        is_visible (bool): A boolean field indicating whether the property offer is visible on the site.
        recommended_offer (bool): A boolean field indicating whether the property should be displayed as a
        recommended offer on the main and properties pages.

    Methods:
        get_absolute_url: Returns the URL to the single property page for the current property instance.

    Meta:
        ordering (tuple): The default ordering for the model. Orders properties by is_visible, recommended_offer,
        realtor, price, and country.
        verbose_name (str): A human-readable name for the model that is singular. In this case, the verbose name is
        set to "3. Property".
        verbose_name_plural (str): A human-readable name for the model that is plural. In this case, the verbose name
        plural is set to "3. Property".
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)
    location_address = models.TextField(max_length=300)
    country = models.CharField(max_length=50)
    price = models.CharField(default=0, help_text='Price in US dollar.', max_length=15)
    description = HTMLField(max_length=1000, blank=True)
    bed_quantity = models.PositiveSmallIntegerField(blank=True)
    baths_quantity = models.PositiveSmallIntegerField(blank=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    is_visible = models.BooleanField(help_text='Is property offer is visible on site.')
    recommended_offer = models.BooleanField(default=False, help_text='This offer will be displayed in '
                                                                     'Popular Properties on Main page and'
                                                                     ' in Featured Properties on Properties page.')

    class Meta:
        ordering = ('is_visible', 'recommended_offer', 'realtor', 'price', 'country', )
        verbose_name = '3. Property'
        verbose_name_plural = '3. Property'

    def get_absolute_url(self):
        """
        Returns the URL to the single property page for the current property instance.

        Returns:
            str: The URL to the single property page.
        """

        return reverse("property_single_page:single_page_view", args=[self.id, self.slug])


class PropertyPhoto(models.Model):
    """
    Model for adding photos to Property models.

    Attributes:
        photo (ImageField): ImageField with upload_to method.
        font_image_of_offer_page (BooleanField): Is the image displayed as the main image for property offer.
        property_item (ForeignKey): ForeignKey to Property model.

    Methods:
        get_file_name (function): Function to rename the photo file with unique filename.
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
        return os.path.join('property_photos/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    font_image_of_offer_page = models.BooleanField(default=False)
    property_item = models.ForeignKey(Property, on_delete=models.CASCADE)


class OurBenefits(models.Model):
    """
       Model representing the benefits of using the website.

   Attributes:
       header (TextField): a text field for the header of the benefits section, which can be up to 200 characters long.
       heading_text (TextField): a text field for the main text of the benefits section, which can be up to 300
        characters long.
       house_point_header (CharField): a character field for the header of the house-related benefit, which can be
        up to 500 characters long.
       house_point_heading_text (CharField): a character field for the main text of the house-related benefit, which
        can be up to 500 characters long.
       agents_point_header (CharField): a character field for the header of the agents-related benefit, which can be up
        to 500 characters long.
       agents_point_heading_text (CharField): a character field for the main text of the agents-related benefit, which
        can be up to 500 characters long.
       safety_point_header (CharField): a character field for the header of the safety-related benefit, which can be
        up to 500 characters long.
       safety_point_heading_text (CharField): a character field for the main text of the safety-related benefit, which
        can be up to 500 characters long.
       image (ImageField): an image field for the benefit section image, which is uploaded to the 'our_benefits/'
       directory.
       block_1_header_number (CharField): a character field for the number of the first benefit block's header, which
       can be up to 10 characters long.
       block_1_heading_text (CharField): a character field for the main text of the first benefit block's header, which
        can be up to 100 characters long.
       block_2_header_number (CharField): a character field for the number of the second benefit block's header, which
       can be up to 10 characters long.
       block_2_heading_text (CharField): a character field for the main text of the second benefit block's header,
        which can be up to 100 characters long.
       block_3_header_number (CharField): a character field for the number of the third benefit block's header, which
       can be up to 10 characters long.
       block_3_heading_text (CharField): a character field for the main text of the third benefit block's header, which
        can be up to 100 characters long.
       block_4_header_number (CharField): a character field for the number of the fourth benefit block's header,
       which can be up to 10 characters long.
       block_4_heading_text (CharField): a character field for the main text of the fourth benefit block's header,
       which can be up to 100 characters long.
   """

    def get_file_name(self, filename: str) -> str:
        """
       Method that generates a unique filename for the benefit section image.

       Args:
           filename (str): the original filename of the uploaded image.

       Returns:
           A string with the new filename, which includes a UUID and the original file extension.
       """

        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('our_benefits/', new_filename)

    header = models.TextField(max_length=200)
    heading_text = models.TextField(max_length=300)
    house_point_header = models.CharField(max_length=500)
    house_point_heading_text = models.CharField(max_length=500)
    agents_point_header = models.CharField(max_length=500)
    agents_point_heading_text = models.CharField(max_length=500)
    safety_point_header = models.CharField(max_length=500)
    safety_point_heading_text = models.CharField(max_length=500)
    image = models.ImageField(upload_to=get_file_name)
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
       Method that returns a string representation of the benefits section header.

       Returns:
           A string with the first 50 characters of the header, or the full header if it is less than 50 characters long.
       """
        if len(self.header) > 50:
            return f'{self.header[:50]}'
        else:
            return f'{self.header}'

    class Meta:
        """
        Additional metadata about the model.

        Attributes:
            verbose_name (str): A human-readable name for the model that is singular. In this case, the verbose name is set to "4. Our benefits".
            verbose_name_plural (str): A human-readable name for the model that is plural. In this case, the verbose name plural is set to "4. Our benefits".
        """

        verbose_name = '4. Our benefits'
        verbose_name_plural = '4. Our benefits'


class CustomerSays(models.Model):
    """
    Model representing customer comments and feedback.

    Attributes:
        photo (ImageField): an image field for the customer's photo, which is uploaded to the 'customer_says/'
        directory.
        name (CharField): a character field for the customer's name.
        comment (TextField): a text field for the customer's comment, which can be up to 1000 characters long.
        customer_position (CharField): a character field for the customer's position or job title.
        is_visible (BooleanField): a boolean field that determines whether the comment is visible on the site.
        The default is True.
    """

    def get_file_name(self, filename: str) -> str:
        """
       Method that generates a unique filename for each customer comment photo.

       Args:
           filename (str): the original filename of the uploaded photo.

       Returns:
           A string with the new filename, which includes a UUID and the original file extension.
       """
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('customer_says/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    name = models.CharField(max_length=200)
    comment = models.TextField(max_length=1000)
    customer_position = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=True, help_text='Is comment visible on site.')

    def __str__(self):
        """
        Method that returns a string representation of the customer's name.

        Returns:
            A string with the customer's name.
        """

        return f'{self.name}'

    class Meta:
        """
        Meta options for the CustomerSays model.

        Attributes:
            verbose_name (str): a string representing the singular name of the model in the Django admin interface.
            verbose_name_plural (str): a string representing the plural name of the model in the Django admin interface.
        """

        verbose_name = '5. Customer says'
        verbose_name_plural = '5. Customer says'
