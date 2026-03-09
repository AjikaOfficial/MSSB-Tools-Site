from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Abilities"


class Character(models.Model):

    TYPE_CHOICES = {
        "BALANCE": "Balance",
        "TECHNIQUE": "Technique",
        "SPEED": "Speed",
        "POWER": "Power",
    }

    STAR_PITCH_CHOICES = {
        "FASTBALL": "Fastball",
        "CHANGEUP": "Changeup",
        "CURVEBALL": "Curveball",
    }

    STAR_SWING_CHOICES = {
        "POP_FLY": "Pop Fly",
        "GROUNDER": "Grounder",
        "LINE_DRIVE": "Line Drive",
    }

    HORIZONTAL_HIT_TRAJECTORY_CHOICES = {
        "PULL": "Pull",
        "MID": "Mid",
        "PUSH": "Push",
    }

    VERTICAL_HIT_TRAJECTORY_CHOICES = {
        "HIGH": "High",
        "MID": "Mid",
        "LOW": "Low",
    }

    name = models.CharField(max_length=32, unique=True)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES)
    curve_ball_speed = models.PositiveSmallIntegerField()
    fast_ball_speed = models.PositiveSmallIntegerField()
    curve = models.PositiveSmallIntegerField()
    cursed_ball = models.PositiveSmallIntegerField(default=50)
    throw_power = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    slap_hit_power = models.PositiveSmallIntegerField()
    charge_hit_power = models.PositiveSmallIntegerField()
    bunting = models.PositiveSmallIntegerField()
    height = models.FloatField()
    dive_range = models.FloatField()
    bat_reach = models.PositiveSmallIntegerField()
    full_charge_frames = models.PositiveSmallIntegerField()
    wall_splat = models.BooleanField(default=False)
    curved_hits = models.BooleanField(default=False)
    trimmed_bat = models.BooleanField(default=False)

    abilities = models.ManyToManyField(Ability, related_name="characters")
    star_pitch = models.CharField(max_length=16, choices=STAR_PITCH_CHOICES)
    star_swing = models.CharField(max_length=16, choices=STAR_SWING_CHOICES)
    horizontal_hit_trajectory = models.CharField(
        max_length=4, choices=HORIZONTAL_HIT_TRAJECTORY_CHOICES
    )
    vertical_hit_trajectory = models.CharField(
        max_length=4, choices=VERTICAL_HIT_TRAJECTORY_CHOICES
    )

    chemistry = models.ManyToManyField("self", blank=True)
    anti_chemistry = models.ManyToManyField("self", blank=True)
    main_variant = models.BooleanField(default=True)
    variants = models.ManyToManyField("self", blank=True)

    icon = models.ImageField(upload_to="character_icons/", blank=True, null=True)
    portrait = models.ImageField(upload_to="character_portraits/", blank=True, null=True)

    def __str__(self):
        return self.name
    
    def is_captain(self):
        return False


class Captain(Character):
    captain_star_ability = models.CharField(max_length=16)

    def is_captain(self):
        return True