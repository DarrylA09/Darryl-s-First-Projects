from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    """
    This class creates a view for signing up a user.
    """
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"