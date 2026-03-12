from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class ImageResource(resources.ModelResource):
    class Meta:
        model = Image

class ImageAdmin(ImportExportModelAdmin):
    resource_class = ImageResource

admin.site.register(Image, ImageAdmin)