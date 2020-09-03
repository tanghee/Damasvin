from django.db import models


class Drink(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True, upload_to='menu/%Y/%m/%d/')

    def __str__(self):
        return f'카테고리: {self.category}, 이름: {self.name}, 가격: {self.price}'

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    pass