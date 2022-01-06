from django.core.paginator import Paginator
from django.db.models import F
from django.shortcuts import render
from zen_queries import render as zen_render, fetch

from shop.models import Order


def slow_orders(request):

    all_orders = Order.objects.all()
    paginator = Paginator(all_orders, 10)
    page = paginator.get_page(request.GET.get("page"))

    return render(
        request, "orders.html", {"orders": page.object_list, "page_obj": page}
    )


def fast_orders(request):
    all_orders = Order.objects.select_related(
        "customer",
        "customer__address",
        "customer__auth_user",
        "pizza",
    ).prefetch_related("pizza__pizzatopping_set", "pizza__pizzatopping_set__topping")
    paginator = Paginator(all_orders, 10)
    page = paginator.get_page(request.GET.get("page"))

    return render(
        request, "orders.html", {"orders": page.object_list, "page_obj": page}
    )


def unzen_orders(request):

    all_orders = Order.objects.all()
    paginator = Paginator(all_orders, 10)
    page = paginator.get_page(request.GET.get("page"))

    return zen_render(
        request, "orders.html", {"orders": page.object_list, "page_obj": page}
    )


def zen_orders(request):
    all_orders = fetch(
        Order.objects.select_related(
            "customer",
            "customer__address",
            "customer__auth_user",
            "pizza",
        ).prefetch_related(
            "pizza__pizzatopping_set", "pizza__pizzatopping_set__topping"
        )
    )
    paginator = Paginator(all_orders, 10)
    page = paginator.get_page(request.GET.get("page"))

    return zen_render(
        request, "orders.html", {"orders": page.object_list, "page_obj": page}
    )
