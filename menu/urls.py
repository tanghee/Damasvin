from django.urls import path

from menu.views import DrinkListView

app_name = 'menu'

urlpatterns = [
    path('', DrinkListView.as_view(), name='list'),
]