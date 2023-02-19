from django.db import models
from django.core.validators import RegexValidator
from tinymce.models import HTMLField


# Create your models here.


class ContactUs(models.Model):
    """
    Model to store contact requests.

    Attributes:
        name (str): Name of the person who made the request.
        email (str): Email of the person who made the request.
        subject (str): Subject of the request.
        message (str): Message of the request.
        date_of_the_request (datetime): Date and time of the request.
        is_processed (bool): Flag indicating if the request has been processed.
    """

    email_re = RegexValidator(regex=r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}'
                                    r'([a-z0-9-]*[a-z0-9])?$', message='Standard e-mail form')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=63, validators=[email_re])
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=1000, blank=True)
    date_of_the_request = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        """
        Metadata for the ContactUs model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """

        ordering = ('-date_of_the_request', )
        verbose_name = '1. Contact Requests'
        verbose_name_plural = '1. Contact Requests'

    def __str__(self):
        """
        Returns a string representation of a ContactUs object.

        Returns:
            str: The string representation of a ContactUs object, which consists of the person's name, email, and
                the subject of their request.
        """

        return f'{self.name}, {self.email} - {self.subject}'


class ContactInfoLeft(models.Model):
    """
    Model to store contact information.

    Attributes:
        location (str): The location of the company.
        open_hours (str): The open hours of the company.
        email (str): The email of the company.
        call (str): The phone number of the company.
    """

    location = HTMLField(max_length=200)
    open_hours = HTMLField(max_length=200)
    email = HTMLField(max_length=200)
    call = HTMLField(max_length=200)
    phone_for_footer = models.CharField(max_length=30)

    class Meta:
        """
        Metadata for the ContactInfoLeft model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """
        verbose_name = '2. Contact info block'
        verbose_name_plural = '2. Contact info block'

    def __str__(self):
        """
        Returns a string representation of a ContactInfoLeft object.

        Returns:
            str: The string representation of a ContactInfoLeft object, which consists of the string 'Info block'
                followed by the object's primary key.
        """

        return f'Info block {self.pk}'


class Sources(models.Model):
    """
    Model to store the source links for your web application.

    Fields:
    - source: the name or title of the source (HTMLField, max length 200).
    - source_url: the URL of the source (URLField).
    """

    source = HTMLField(max_length=200)
    source_url = models.URLField()

    class Meta:
        """
        Metadata for the ContactInfoLeft model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """
        verbose_name = '3. Sources'
        verbose_name_plural = '3. Sources'

    def __str__(self):
        """
        Returns a string representation of a ContactInfoLeft object.

        Returns:
            str: The string representation of a ContactInfoLeft object, which consists of the string 'Info block'
                followed by the object's primary key.
        """

        return f'Source {self.pk}'


class MediaLinks(models.Model):
    """
    Model for storing links to various social media profiles.

    Fields:
        - instagram: URLField to store the link to the Instagram profile.
        - twitter: URLField to store the link to the Twitter profile.
        - facebook: URLField to store the link to the Facebook profile.
        - linkedin: URLField to store the link to the LinkedIn profile.
        - pinterest: URLField to store the link to the Pinterest profile.
        - dribbble: URLField to store the link to the Dribbble profile.
    """

    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    pinterest = models.URLField(blank=True)
    dribbble = models.URLField(blank=True)

    class Meta:
        """
        Metadata for the ContactInfoLeft model.

        Attributes:
           verbose_name (str): The human-readable name for a single object of the model.
           verbose_name_plural (str): The human-readable name for multiple objects of the model.
        """
        verbose_name = '4. Media links'
        verbose_name_plural = '4. Media links'

    def __str__(self):
        """
        Returns a string representation of a ContactInfoLeft object.

        Returns:
            str: The string representation of a ContactInfoLeft object, which consists of the string 'Info block'
                followed by the object's primary key.
        """

        return f'Block of links {self.pk}'
