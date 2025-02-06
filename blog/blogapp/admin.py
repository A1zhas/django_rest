from django.contrib import admin
from django.db.models import F
from .models import Category, Post, Tag
# Register your models here.

admin.site.register(Category)

def clear_rating(modeladmin, request, queryset):
    queryset.update(rating=1)

clear_rating.short_description = 'выставить рейтинг = 1'

def set_active(modeladmin, request, queryset):
    # for item in queryset:
    #     item.is_active=True
    #     item.save()

    # bulk update
    queryset.update(is_active=True)


def reverse_is_active(modeladmin, request, queryset):
    for item in queryset:
        item.is_active = not item.is_active
        item.save()

    # bulk update
    # queryset.update(is_active=F('is_active'))

    #
    # Post.filter(name = F('id'))

def add_rating(modeladmin, request, queryset):
    # for item in queryset:
    #     item.rating =  item.rating + 1
    #     # item.rating += 1
    #     item.save()

    # bulk update
    queryset.update(rating=F('rating') + 1)
    # update post set rating = rating + 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'category', 'display_tags', 'has_image', 'rating', 'is_active']
    actions = [clear_rating, set_active, reverse_is_active, add_rating]


admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]


admin.site.register(Tag, TagAdmin)