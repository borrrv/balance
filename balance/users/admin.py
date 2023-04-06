from django.contrib import admin

from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'id',
        'email',
    )
    search_fields = (
        'id',
        'email',
    )


admin.site.register(Users, UsersAdmin)
