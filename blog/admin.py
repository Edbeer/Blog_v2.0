from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}

    list_display = ('id', 'title', 'slug', 'category',
                    'created_at', 'views', 'get_photo', 'is_published')
    list_display_links = ('id', 'title', 'slug')
    list_filter = ('category', 'tags', 'is_published')
    list_editable = ('is_published',)

    fields = ('title', 'slug', 'content', 'photo', 'get_photo',
              'category', 'tags', 'views', 'created_at', 'is_published')
    readonly_fields = ('get_photo', 'views', 'created_at')
    search_fields = ('title', 'content')

    save_on_top = True
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75>')

    get_photo.short_description = 'image'


class AdminComment(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'user', 'post', 'created_at')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'post')


class AdminTag(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, AdminComment)
admin.site.register(Tag, AdminTag)
admin.site.register(Category, AdminCategory)
