from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import DishCategory, Dish, FooterItem, Event, Gallery, Chef, Contact, Reservation

# Регистрация остальных моделей
admin.site.register(FooterItem)
admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Reservation)


# Классы администратора
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'description', 'price', 'is_visible', 'position')
    list_editable = ('name', 'position', 'is_visible', 'description', 'price')
    prepopulated_fields = {'slug': ('name',)}

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Фото мероприятия'


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'is_visible')
    list_editable = ('name', 'position', 'is_visible')

    # Встраивание для блюд
    class DishInline(admin.TabularInline):
        model = Dish
        extra = 0

    inlines = [DishInline]


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'slug', 'ingredients', 'description', 'price', 'is_visible', 'position', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('ingredients', 'price', 'is_visible', 'position')
    list_filter = ('category', 'is_visible')
    search_fields = ('name', 'ingredients', 'description')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Фото блюда'


# Класс администратора для модели Chef
@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('photo_thumbnail', 'name', 'job_title',)
    list_editable = ('name', 'job_title',)
    readonly_fields = ('photo_thumbnail',)

    def photo_thumbnail(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 100px; max-width: 100px;" />')
        else:
            return 'No Photo'
    photo_thumbnail.short_description = 'Thumbnail'
