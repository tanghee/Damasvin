from django.db import models

from menu.models import Drink


class Order(models.Model):
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='order')  # Drink에서 값이 지워지면 이곳의 값도 지우겠다는 뜻
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=1)
    cup = models.IntegerField(default=0)  # 0: 레귤러, 1: 점보(+500)
    ice = models.IntegerField(default=100)  # 0%, 50%, 100%, 150%
    sugar = models.IntegerField(default=100)  # 0%, 50%, 100%, 150%
    pearl = models.CharField(max_length=10, default="타피오카")  # 타피오카펄, 코코펄, 곤약젤리펄, 알로에펄

    def __str__(self):
        _CUPS = ['레귤러', '점보']
        result = f'음료: {self.drink.name}, 가격: {self.price}, 수량: {self.stock}, ' \
                 f'컵 SIZE: {_CUPS[self.cup]}, 얼음량: {self.ice}%, 당도: {self.sugar}%'
        if self.drink.category == 'Bubbletea':
            result += f', 펄: {self.pearl}'
        return result
