from django.contrib import admin

from .models import Order, Service, Revenue


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


class RevenueAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'price',
        'service',
    )
    list_filter = (
        'user',
    )
    search_fields = (
        'user',
    )

admin.site.register(Revenue, RevenueAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
