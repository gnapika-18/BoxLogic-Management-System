
from django.test import TestCase
from decimal import Decimal
from .models import Product


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            length=Decimal("30.00"),
            width=Decimal("20.00"),
            height=Decimal("5.00"),
            weight=Decimal("2.00")
        )

    
    def test_product_creation(self):
        self.assertEqual(Product.objects.count(), 1)

    
    def test_product_name(self):
        self.assertEqual(self.product.name, "Laptop")

    def test_product_dimensions(self):
        self.assertEqual(self.product.length, Decimal("30.00"))
        self.assertEqual(self.product.width, Decimal("20.00"))
        self.assertEqual(self.product.height, Decimal("5.00"))

    def test_product_weight(self):
        self.assertEqual(self.product.weight, Decimal("2.00"))

    def test_product_str(self):
        self.assertEqual(str(self.product), "Laptop")
