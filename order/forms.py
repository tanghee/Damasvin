from django import forms

from order.models import Order


class OrderModelForm(forms.ModelForm):
    _CUPS = (('0', '레귤러'), ('1', '점보'))
    _ICES = (('0', '0%'), ('50', '50%'), ('100', '100%'), ('150', '150%'))
    _SUGARS = (('0', '0%'), ('50', '50%'), ('100', '100%'), ('150', '150%'))
    _PEARLS = (('타피오카펄', '타피오카펄'), ('코코펄', '코코펄'), ('곤약젤리펄', '곤약젤리펄'), ('알로에펄', '알로에펄'))
    cup = forms.ChoiceField(widget=forms.Select, choices=_CUPS, initial=0)
    ice = forms.ChoiceField(widget=forms.RadioSelect, choices=_ICES, initial=100)
    sugar = forms.ChoiceField(widget=forms.RadioSelect, choices=_SUGARS, initial=100)
    pearl = forms.ChoiceField(widget=forms.Select, choices=_PEARLS, initial='타피오카펄')

    class Meta:
        model = Order
        fields = ['drink', 'cup', 'ice', 'sugar', 'pearl', 'stock', 'price']