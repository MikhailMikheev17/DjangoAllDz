from decimal import Decimal

from django.contrib import admin
from .models import Client, Product, Order

DISCOUNT = 10


@admin.action(description="apply  discount")
def apply_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price -= (product.price * Decimal(DISCOUNT / 100))
        product.save()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'photo']
    ordering = ['-quantity']
    list_filter = ['created_at', 'price', 'quantity']
    search_fields = ['description', 'name']
    search_help_text = 'seach in names and descriptions'
    actions = [apply_discount]
    readonly_fields = ['created_at']
    fieldsets = [
        ('main', {'classes': ['wide'], 'fields': ['name', 'price', 'quantity']}),
        ('description', {'classes': ['collapse'], 'fields': ['description', 'photo']}),
        ('created_at', {'fields': ['created_at']}),
    ]


class OrderAdmin(admin.ModelAdmin):
    @staticmethod
    def get_customer_name(obj):
        return obj.customer.name

    list_display = ['get_customer_name', 'total_amount', 'date_ordered']
    ordering = ['-date_ordered', '-total_amount', ]
    search_fields = ['customer__name', 'total_amount']
    search_help_text = 'seach a customer by name or total amount'
    readonly_fields = ['customer', 'total_amount', 'products']
    list_filter = ['customer', 'total_amount']
    fieldsets = [
        ('main', {'classes': ['wide'], 'fields': ['customer', 'total_amount', 'date_ordered']}),
        ('products', {'classes': ['collapse'], 'fields': ['products']})
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', ]
    search_fields = ['name', 'email', 'phone', 'address']
    search_help_text = 'name, email, phone, address'
    readonly_fields = ['registration_date']
    fieldsets = [
        ('main', {'classes': ['wide'], 'fields': ['name', 'email', 'phone', 'address']}),
        (None, {'fields': ['registration_date']})
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)

# Register your models here.
