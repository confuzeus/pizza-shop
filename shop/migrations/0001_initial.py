# Generated by Django 4.0.1 on 2022-01-06 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("line_1", models.TextField()),
                ("line_2", models.TextField()),
                ("line_3", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=155)),
                (
                    "size",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Small"), (1, "Medium"), (2, "Large")]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Topping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="PizzaTopping",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("extra", models.BooleanField(default=False)),
                (
                    "pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="shop.pizza"
                    ),
                ),
                (
                    "topping",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="shop.topping"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pizza",
            name="toppings",
            field=models.ManyToManyField(
                through="shop.PizzaTopping", to="shop.Topping"
            ),
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="shop.customer",
                    ),
                ),
                (
                    "pizza",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="orders",
                        to="shop.pizza",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="customers",
                to="shop.customeraddress",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="auth_user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="as_customer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
