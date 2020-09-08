from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from menu.models import Drink
from order.models import Order


class OrderListView(ListView):
    model = Order

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # context 를 부모로부터 호출해서 먼저 생성
        context['menu_list'] = Drink.objects.all()
        context['total_price'] = Order.objects.all().aggregate(total_price=Sum('price')).get('total_price', 0)    # aggregate 는 그룹으로 합산해서 계산해주는 함수
        return context


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'   # 모델이 갖고 있는 모든 속성을 다 넣기 위함
    template_name_suffix = '_create'
    success_url = reverse_lazy('order:list')

    def get_initial(self):  # 초기화 해주는 함수. 넘겨주는 값을 받아와야하기 때문에 함수 사용.
        initial = super().get_initial()
        initial['drink'] = self.kwargs.get('menu_id')
        return initial


# CBV : 클래스를 기반으로 한 View, 상속받아서 금방 만들 수 있음
class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('order:list')


# FBV
# Template 작성하지 않고 함수 기반의 뷰를 사용. 바로 삭제를 위함.
def order_delete(request, pk):
    order = Order.objects.get(id=pk)     # DB 값을 꺼내오는 코드
    order.delete()                       # DB 에서 값이 삭제됨.
    return redirect('order:list')


class OrderResultView(ListView):
    model = Order
    template_name_suffix = '_result'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = Order.objects.all().aggregate(total_price=Sum('price')).get('total_price', 0)
        return context
