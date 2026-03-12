from django import template

register = template.Library()


@register.filter
def identifier(value):
    match value:
        case None:
            return ""
        case "Toad":
            return "Red"
        case "Shy Guy":
            return "Red"
        case "Koopa Troopa":
            return "Green"
        case "Koopa Paratroopa":
            return "Red"
        case "Magikoopa":
            return "Blue"
        case "Dry Bones":
            return "Gray"
        case _:
             return value.split(" ", 1)[0]

@register.filter
def badge_color(identifier):
    
    if not identifier:
        return "border-gray-500"
    key = identifier.lower()
    mapping = {
        "red": "border-red-500",
        "blue": "border-blue-500",
        "green": "border-green-500",
        "yellow": "border-yellow-500",
        "purple": "border-purple-500",
        "black": "border-black",
        "hammer": "border-green-500",
        "fire": "border-red-500",
        "boomerang": "border-blue-500",
    }
    if key in mapping:
        return mapping[key]
