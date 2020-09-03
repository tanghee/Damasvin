from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Drink


class DrinkListView(ListView):
    model = Drink