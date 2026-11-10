
from django.test import TestCase
from decimal import Decimal

from products.models import Product
from .models import Order, OrderItem, Box
from .box_selector import recommend_box


class OrderModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=Decimal("30.00"),
            width=Decimal("20.00"),
            height=Decimal("5.00"),
            weight=Decimal("2.00")
        )

        self.order = Order.objects.create(
            customer_name="Gnapika",
            status="pending"
        )

        OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )

    def test_order_creation(self):
        self.assertEqual(Order.objects.count(), 1)

    def test_product_added_to_order(self):
        self.assertEqual(self.order.items.count(), 1)

    def test_suitable_box_recommendation(self):
        box = Box.objects.create(
            name="Large Box",
            length=Decimal("40.00"),
            width=Decimal("30.00"),
            height=Decimal("25.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("40.00")
        )

        result = recommend_box(self.order.id)

        self.assertEqual(result, box)

    def test_no_suitable_box(self):
        Box.objects.create(
            name="Small Box",
            length=Decimal("10.00"),
            width=Decimal("10.00"),
            height=Decimal("10.00"),
            max_weight=Decimal("1.00"),
            cost=Decimal("15.00")
        )

        result = recommend_box(self.order.id)

        self.assertIsNone(result)

    def test_cheapest_box_selection(self):
        Box.objects.create(
            name="Expensive Box",
            length=Decimal("40.00"),
            width=Decimal("30.00"),
            height=Decimal("25.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("60.00")
        )

        cheapest_box = Box.objects.create(
            name="Budget Box",
            length=Decimal("40.00"),
            width=Decimal("30.00"),
            height=Decimal("25.00"),
            max_weight=Decimal("10.00"),
            cost=Decimal("30.00")
        )

        result = recommend_box(self.order.id)

        self.assertEqual(result, cheapest_box)
