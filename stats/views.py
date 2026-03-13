from django.shortcuts import render
from django.db.models import Prefetch
from django.http import Http404
from .models import Character
from django.db.models import PositiveSmallIntegerField, FloatField


def index(request):
    char_list = (
        Character.objects.filter(main_variant=True)
        .order_by("id")
        .only("id", "name", "icon")
        .prefetch_related(
            Prefetch(
                "variants",
                queryset=Character.objects.only("id", "name"),
            )
        )
    )
    return render(request, "stats/index.html", {"char_list": char_list})


def detail(request, char_name):
    unslugged = char_name.replace("-", " ")
    try:
        character = Character.objects.get(name__iexact=unslugged)
    except Character.DoesNotExist:
        raise Http404("Character does not exist")
    
    chem = character.chemistry.filter(main_variant=True).only("id", "name", "icon")
    anti_chem = character.anti_chemistry.filter(main_variant=True).only("id", "name", "icon")
    return render(request, "stats/detail.html", {"character": character, "chem": chem, "anti_chem": anti_chem})