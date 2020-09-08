from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from order.models import Order


class OrderListView(ListView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'   # 모델이 갖고 있는 모든 속성을 다 넣기 위함
    template_name_suffix = '_create'
    success_url = reverse_lazy('order:list')


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
