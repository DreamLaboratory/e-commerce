from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.image_product import ProductImage
from .models.review import Review
from .models.variants import ProductVariants
from django.utils.html import format_html
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImage
    extra = 2



class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("rating", "created_at")
    list_display_links = ('product', 'user')

    raw_id_fields = ("user", 'product')
    date_hierarchy = "created_at"
    list_editable = ("status",)


    def active_status(self, request, queryset):
        queryset.update(status=True)

    active_status.short_description = 'All status Active process'

    def inactive_status(self, reqeust, queryset):
        queryset.update(status=False)

    inactive_status.short_description = 'All status Inactive process'

    actions = ['active_status', 'inactive_status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'is_available', 'created_at', 'updated_at')
    list_display_links = ('image', 'name')
    list_editable = ('is_available',)
    search_fields = ('product',)
    prepopulated_fields = {"slug":('name',)}
    inlines = [ProductImageModelAdmin]

    def image_product(self, object):
        print('assasas')
        if object.image:
            return format_html(
                f'<img src="{object.image.url}" width="45px" height="45px" style="border-radius: 45px;" />'
            )
        else:
            return format_html(
                '<img src="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png" width="40" style="border-radius: 50px;" />'
            )

    image_product.short_description = 'Product Image'

    def is_available_true(self, request, queryset):
        queryset.update(is_available=True)

    is_available_true.short_description = 'True is_available'

    def is_available_false(self, request, queryset):
        queryset.update(is_available=False)

    is_available_false.short_description = 'False is_available'

    actions = ['is_available_true', 'is_available_false']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductVariants)
