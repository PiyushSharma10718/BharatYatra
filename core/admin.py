from django.contrib import admin

# Register your models here.
from core.models import Category, Package, Packageimages, Packagereview, Address, Profile

class PackageimagesAdmin(admin.TabularInline):
    model = Packageimages

class PackageAdmin(admin.ModelAdmin):
    inlines = [PackageimagesAdmin]
    list_display = ['user', 'title', 'category', 'package_image', 'price', 'featured', 'package_status', 'pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class PackagereviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'review', 'rating']

class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['fname', 'phone']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Packagereview, PackagereviewAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Profile, ProfileAdmin)
