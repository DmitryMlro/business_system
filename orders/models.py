from django.db import models
from inventory.models import Product
from users.models import CustomUser
from django.core.exceptions import ValidationError

class Order(models.Model):
    ORDER_TYPE = (
        ('in', 'Incoming'),
        ('out', 'Outgoing'),
    )
    order_type = models.CharField(max_length=3, choices=ORDER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_order_type_display()} - #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

    def save(self, *args, **kwargs):
        order_type = self.order.order_type

        product = self.product

        if self._state.adding:
            if order_type == 'out':
                if product.stock < self.quantity:
                    raise ValidationError(f"Insufficient accessory in stock for {product.name} (there are: {product.stock}, need: {self.quantity})")
                product.stock -= self.quantity
            elif order_type == 'in':
                product.stock += self.quantity

            product.save()

        super().save(*args, **kwargs)
