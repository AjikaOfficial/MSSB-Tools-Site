from django.contrib import admin
from .models import *


class AbilityAdmin(admin.ModelAdmin):
    fields = ["name", "description"]


class CharacterAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "icon",
        "portrait",
        "type",
        "curve_ball_speed",
        "fast_ball_speed",
        "curve",
        "cursed_ball",
        "throw_power",
        "speed",
        "slap_hit_power",
        "charge_hit_power",
        "bunting",
        "height",
        "dive_range",
        "bat_reach",
        "abilities",
        "chemistry",
        "anti_chemistry",
        "main_variant",
        "variants",
        "star_pitch",
        "star_swing",
        "horizontal_hit_trajectory",
        "vertical_hit_trajectory",
        "full_charge_frames",
        "wall_splat",
        "curved_hits",
        "trimmed_bat",
    ]


class CaptainAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "icon",
        "portrait",
        "type",
        "curve_ball_speed",
        "fast_ball_speed",
        "curve",
        "cursed_ball",
        "throw_power",
        "speed",
        "slap_hit_power",
        "charge_hit_power",
        "bunting",
        "height",
        "dive_range",
        "bat_reach",
        "abilities",
        "chemistry",
        "anti_chemistry",
        "main_variant",
        "variants",
        "captain_star_ability",
        "star_pitch",
        "star_swing",
        "horizontal_hit_trajectory",
        "vertical_hit_trajectory",
        "full_charge_frames",
        "wall_splat",
        "curved_hits",
        "trimmed_bat",
    ]


admin.site.register(Ability, AbilityAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Captain, CaptainAdmin)
