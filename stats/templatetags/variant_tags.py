from django import template

register = template.Library()


@register.filter
def identifier(value):
    if not value:
        return ""
    return value.split(" ", 1)[0]


@register.filter
def badge_color(identifier):
    """Return a Tailwind border colour class for the given variant identifier.

    We keep a whitelist of known colour names; anything else falls back to
    a neutral border.  The identifier is expected to already be normalized
    (e.g. from the ``identifier`` filter).  This allows templates to do
    ``{{ variant.name|identifier|badge_color }}`` and insert the result
    into the ``class`` attribute.
    """
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
        "fire": "border-red-500",
        "boomerang": "border-green-500",
    }
    if key in mapping:
        return mapping[key]
