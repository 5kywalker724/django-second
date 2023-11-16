from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


def index(request):
    return render(request, 'applications/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'applications/register.html'
    success_url = reverse_lazy('login')
