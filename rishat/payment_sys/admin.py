from django.contrib import admin

from payment_sys.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Класс представления товаров в админке."""
    list_display = ("pk", "name", "description", "price")
    search_fields = ('name',)
    empty_value_display = '-пусто-'
