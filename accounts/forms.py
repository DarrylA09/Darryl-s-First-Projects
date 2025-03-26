from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    """
    This class creates a form that includes a firstname for signing up a user
    """
    first_name = forms.CharField(max_length=100)

    class meta:
        """
        This class defines the fields that are included in the form.
        """
        model = User
        fields = ('username', 'firstname', 'password1', 'password2')