from django.contrib import admin

from .models import Order, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'owner_id',
    )


admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
