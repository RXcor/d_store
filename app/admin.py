from django.contrib import admin
from app.models import Basket, Position, Product, Role
from users.models import CustomUser

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'last_name', 'first_name', 'middle_name', 'role', 'is_active', 'delivery_address')
#
#     def role(self, obj):
#         return "\n".join([role.title for role in obj.role.all()])

class PositionInline(admin.TabularInline):
    model = Position

class BasketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'active')

    inlines = [
        PositionInline,
    ]




class PositionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number', 'amount', 'basket')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('vendor_code', 'title', 'purchase_price', 'retail_price')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','title')


admin.site.register(Role, RoleAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(CustomUser, CustomUserAdmin)
