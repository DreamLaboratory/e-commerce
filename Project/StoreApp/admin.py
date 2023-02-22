from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.image_product import ProductImage
from .models.review import Review
from .models.variants import ProductVariants
from django.utils.html import format_html
import admin_thumbnails
from import_export import resources
from import_export.admin import ImportExportModelAdmin


@admin_thumbnails.thumbnail('image')
class ProductImageModelAdmin(admin.TabularInline):
    model = ProductImage
    extra = 2


@admin.register(Review)
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


class ResourceProduct(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity')


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ResourceProduct
    list_display = ('image', 'name', 'is_available', 'created_at', 'updated_at')
    list_display_links = ('image', 'name')
    list_editable = ('is_available',)
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ('name',)}
    inlines = [ProductImageModelAdmin]

    def image_product(self, object):
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


######## Category
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('name', 'created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ('name',)}
    date_hierarchy = "created_at"


admin.site.register(ProductImage)
admin.site.register(ProductVariants)
