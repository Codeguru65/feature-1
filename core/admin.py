from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class VehicleAdmin(ImportExportModelAdmin):
    class VehicleResource(resources.ModelResource):
        class Meta:
            model=Vehicle    
    resource_class=VehicleResource


class PackageRateAdmin(ImportExportModelAdmin):
    class PakageRateReource(resources.ModelResource):
        class Meta:
            model=PackageRate
    resource_class=PakageRateReource


class UseCaseAdmin(ImportExportModelAdmin):
    class UseCaseResource(resources.ModelResource):
        model = UseCase
    resource_class=UseCaseResource
    

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(PackageRate, PackageRateAdmin)
admin.site.register(UseCase, UseCaseAdmin)