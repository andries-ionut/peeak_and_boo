from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView

from produse.models import ProduseModel


# Create your views here.


class Produseview(ListView):
    template_name = "product.html"
    model = ProduseModel
    # success_url = reverse_lazy("")
