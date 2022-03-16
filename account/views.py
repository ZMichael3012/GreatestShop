from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    next_page = reverse_lazy('homepage')


class AccountView(DetailView):
    pass
