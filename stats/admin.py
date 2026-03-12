from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
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

    filter_horizontal = ["abilities", "chemistry", "anti_chemistry", "variants"]


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

    filter_horizontal = ["abilities", "chemistry", "anti_chemistry", "variants"]


class CharacterResource(resources.ModelResource):
    class Meta:
        model = Character
class CharacterBulkAdmin(ImportExportModelAdmin):
    resource_class = CharacterResource

class CaptainResource(resources.ModelResource):
    class Meta:
        model = Captain
class CaptainBulkAdmin(ImportExportModelAdmin):
    resource_class = CaptainResource

admin.site.register(Ability, AbilityAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Captain, CaptainAdmin)
# admin.site.register(Character, CharacterBulkAdmin)
# admin.site.register(Captain, CaptainBulkAdmin)
