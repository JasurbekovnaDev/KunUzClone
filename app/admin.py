<<<<<<< HEAD
# from django.contrib import admin
#
# from app.models import Blog
#
# # Register your models here.
#
# admin.site.register(Blog)


from django.contrib import admin

from app.models import News, Category, ContactData, Contact, Comment

# Register your models here.

# admin.site.register(News)
# admin.site.register(Category)
admin.site.register(Contact)

=======
from tkinter import Image
from django.contrib import admin
from app.models import News,Category

# Register your models here.

# 1 - способ

# admin.site.register(Category)
# admin.site.register(News)
>>>>>>> 35b99e54e67e3aa1ffd73e07756b09f25fa2da05

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'category']
    list_filter = ['status', 'created_time', 'publish_time']
<<<<<<< HEAD
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title', ]
=======
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['']
    ordering = ['title']
>>>>>>> 35b99e54e67e3aa1ffd73e07756b09f25fa2da05


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


<<<<<<< HEAD
admin.site.register(ContactData)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'active_comments']

    def diasble_comments(self, request, queryset):
        queryset.update(active=False)

    def active_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)
=======

>>>>>>> 35b99e54e67e3aa1ffd73e07756b09f25fa2da05
