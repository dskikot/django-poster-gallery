from django.contrib import admin
from .models import Tag, Image, Category
from django.utils.safestring import mark_safe


class ImageAdmin(admin.ModelAdmin):
    # form = ImageAdminForm
    save_on_top = True
    list_display = ('id', 'title', 'category', 'get_image',)
    list_display_links = ('id', 'title')
    list_filter = ('category', 'tags')
    list_editable = ('category',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)
    fields = ('title', 'category', 'tags', 'filename', 'get_image')

    def get_image(self, obj):
        if obj.filename:
            return mark_safe(f'<img src="{obj.filename.url}" width="60">')
        return '---'

    get_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)


