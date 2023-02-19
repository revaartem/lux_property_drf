from django import forms

from contact_us.models import ContactUs


class ContactForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Your Name',
        })
    )

    email = forms.CharField(
        max_length=63,
        widget=forms.TextInput(attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Your Email',
        })
    )

    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Subject',
        })
    )

    message = forms.CharField(
        max_length=250,
        widget=forms.Textarea(attrs={
            'name': '',
            'id': '',
            'cols': '30',
            'rows': '7',
            'class': 'form-control',
            'placeholder': 'Message',
        })
    )

    class Meta:

        model = ContactUs
        fields = ('name', 'email', 'subject', 'message')