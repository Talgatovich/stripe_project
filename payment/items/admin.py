from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "currency")
    list_filter = ("name", "price")
    search_fields = ("name",)
    empty_value_display = "-пусто-"
