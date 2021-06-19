from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'sign-up.html'