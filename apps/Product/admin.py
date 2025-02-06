from django.contrib import admin
from .models import Category, Product, Favorite


# admin -> category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {
            'fields': ('name', 'icon')
        }),
        ('Дата создания и обновления', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# admin -> product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "currency", "created_at", "updated_at")
    list_filter = ("category", "currency", "created_at", "updated_at")
    search_fields = ("title", "description", "category__name")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'price', 'currency', 'location', 'category', 'image', 'owner')
        }),
        ('Дата создания и обновления', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


# admin -> favorite
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "added_at")
    list_filter = ("user", "product")
    search_fields = ("user__username", "product__title")
    ordering = ("-added_at",)
    readonly_fields = ("added_at",)

    fieldsets = (
        (None, {
            'fields': ('user', 'product')
        }),
        ('Дата добавления', {
            'fields': ('added_at',),
            'classes': ('collapse',)
        }),
    )
