from django.contrib import admin

from .models import Service, Order


# class OrderServiceInline(admin.TabularInline):
#     model = OrderService
#     min_num = 1
#     extra = 1

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
