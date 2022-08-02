from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from core.models import User
class myUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'custom Field',
            {
                'fields':(
                'age',
                'weight',
                'height',
                'kind_user',
                )
            },
        ),
    )

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','kind_user')
UserAdmin.search_fields = ('username', 'first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(User, myUserAdmin)
