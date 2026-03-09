from django.shortcuts import render
from django.db.models import Prefetch
from .models import Character


def index(request):
    char_list = (
        Character.objects.filter(main_variant=True)
        .order_by("id")
        .only("id", "name", "icon")  # only load these columns
        .prefetch_related(
            Prefetch(
                "variants",
                queryset=Character.objects.only("id", "name"),
            )
        )
    )
    return render(request, "stats/index.html", {"char_list": char_list})
