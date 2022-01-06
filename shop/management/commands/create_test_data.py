import random

from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from shop import models

User = get_user_model()

fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):

        for _ in range(10):
            models.CustomerAddress.objects.create(
                line_1=fake.street_address(), line_2=fake.city(), line_3=""
            )

        for _ in range(50):
            models.Topping.objects.create(name=fake.sentence())

        for _ in range(100):
            user = User.objects.create(
                username=fake.user_name(), email=fake.ascii_email()
            )
            customer_address = models.CustomerAddress.objects.order_by("?").first()
            customer = models.Customer.objects.create(
                auth_user=user, address=customer_address
            )

            pizza = models.Pizza.objects.create(
                name=fake.word(), size=random.choice((0, 1, 2))
            )
            for _ in range(4):
                topping = models.Topping.objects.order_by("?").first()
                models.PizzaTopping.objects.create(
                    pizza=pizza, topping=topping, extra=random.choice((True, False))
                )
            models.Order.objects.create(customer=customer, pizza=pizza)
