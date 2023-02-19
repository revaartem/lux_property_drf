from django import forms
from django.contrib.auth import authenticate


class UserLogin(forms.Form):
    """
    Class for creating correct form User Login on the page.

    """
    username = forms.CharField(widget=forms.TextInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'Username',
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'Password',
        }))

    def clean(self):
        """
        Function checked for equality password and login with data in database.

        If all OK - return function clear.
        Other way will return ValidationError.

        :return: function clean() or exception.
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('Error in Login or Password')
        else:
            raise forms.ValidationError('Error in Login or Password')
        return super().clean()