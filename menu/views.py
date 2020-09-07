from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from menu.models import Drink, Coffee, Bubbletea


class DrinkListView(ListView):
    model = Drink


class CoffeeCreateView(CreateView):
    model = Coffee
    fields = '__all__'  # ['category', 'name', 'price', 'image']
    template_name = 'menu/drink_create.html'  # 템플릿을 넣을 때는 App 이름 작성
    success_url = reverse_lazy('menu:list')  # html 은 url 로 하겠지만, 지금은 class 이므로 reverse_lazy 함수 사용. 패스 이름 작성


class BubbleteaCreateView(CreateView):
    model = Bubbletea
    fields = '__all__'
    template_name = 'menu/drink_create.html'
    success_url = reverse_lazy('menu:list')


class DrinkUpdateView(UpdateView):
    model = Drink
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('menu:list')


class DrinkDeleteView(DeleteView):
    model = Drink
    # delete 는 입력하는게 아니므로 필드가 필요없다.
    success_url = reverse_lazy('menu:list')
