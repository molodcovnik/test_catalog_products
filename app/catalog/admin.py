from django.contrib import admin
from catalog.models import Product


@admin.register(Product)
class BonusTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "price",
    )
    ordering = ("-date_added", )
