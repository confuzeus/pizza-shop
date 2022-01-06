from django.db import models
from django.conf import settings


class CustomerAddress(models.Model):
    line_1 = models.TextField()
    line_2 = models.TextField()
    line_3 = models.TextField()


class Customer(models.Model):
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="as_customer"
    )
    address = models.ForeignKey(
        CustomerAddress, on_delete=models.PROTECT, related_name="customers"
    )


class Topping(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    SIZE_CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    )
    name = models.CharField(max_length=155)
    size = models.PositiveSmallIntegerField(choices=SIZE_CHOICES)
    toppings = models.ManyToManyField(Topping, through="PizzaTopping")

    def __str__(self):
        return f"{self.get_size_display()} {self.name}"


class PizzaTopping(models.Model):
    topping = models.ForeignKey(
        Topping,
        on_delete=models.PROTECT,
    )
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.PROTECT,
    )
    extra = models.BooleanField(default=False)


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="orders"
    )
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT, related_name="orders")
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order by {self.customer.auth_user.username} on {self.date}"
