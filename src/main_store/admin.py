from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main_store.models import User, Items, Pictures


class CustomUserAdmin(UserAdmin):
    list_display = ("email", "name", "surname", "role", "is_active")
    list_filter = ("is_active", "role")
    search_fields = ("email", "name", "surname")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "surname",
                    "patronymic",
                    "avatar",
                    "city",
                    "street",
                    "house",
                    "corps",
                    "apartment",
                    "phone_number",
                    "date_of_birth",
                )
            },
        ),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role", "is_active", "is_staff", "is_superuser"),
            },
        ),
    )


class PicturesAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "display_picture")
    list_filter = ("item",)
    search_fields = ("item__name",)
    raw_id_fields = ("item",)

    def display_picture(self, obj):
        return obj.picture.url if obj.picture else None

    display_picture.short_description = "Picture"


class PicturesInline(admin.TabularInline):
    model = Pictures
    extra = 1


class ItemsAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "size", "price")
    list_filter = ("category",)
    search_fields = ("name", "category")
    ordering = ("name",)
    inlines = [PicturesInline]
    fields = ("name", "number", "size", "price", "description", "category")


admin.site.register(User, CustomUserAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Pictures, PicturesAdmin)
