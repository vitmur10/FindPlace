from django.contrib.sites import requests
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .form import UserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


class MainView(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        if requests.user.is_autheticated:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/in/login/'

    template_name = 'Login_in/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = 'Login_in/login.html'

    success_url = '/'

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.user = None

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
