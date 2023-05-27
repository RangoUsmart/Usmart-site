from django.contrib import admin
from .models import Post, Theme
# Register your models here.

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Theme, ThemeAdmin)

class PostAdmin(admin.ModelAdmin):
        list_display =('title', 'description')
        prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
