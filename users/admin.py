from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'last_name', 'first_name', 'middle_name', 'role', 'is_active', 'delivery_address',)

    #
    #     def role(self, obj):
    #         return "\n".join([role.title for role in obj.role.all()])
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name', 'middle_name', 'delivery_address', )}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'last_name', 'first_name', 'middle_name', 'role', 'is_active', 'is_staff', 'delivery_address')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def role(self, obj):
            return "\n".join([role.title for role in obj.role.all()])

admin.site.register(CustomUser, CustomUserAdmin)
