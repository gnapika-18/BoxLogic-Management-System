
from django.shortcuts import render
from .models import Order, OrderItem
from .box_selector import recommend_box


def order_list(request):
    orders = Order.objects.all()

    return render(
        request,
        'orders/order_list.html',
        {'orders': orders}
    )


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)

    order_items = OrderItem.objects.filter(order=order)

    recommended_box = recommend_box(order_id)

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order,
            'order_items': order_items,
            'recommended_box': recommended_box
        }
    )
