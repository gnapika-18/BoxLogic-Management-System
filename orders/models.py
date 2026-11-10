from django.db import models

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} (Status: {self.status})"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order Item {self.id} - {self.product.name} (Quantity: {self.quantity})"

class Box(models.Model):
    name = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    max_weight = models.FloatField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name