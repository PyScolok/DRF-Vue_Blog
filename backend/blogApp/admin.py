from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blogApp.models import Post, Category, Tag, Like, Comment


class PostAdminForm(forms.ModelForm):
    """Виджет ckeditor"""

    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    """Посты"""

    list_display = ("title", "author", "publish", "update", "category", "get_image", "is_draft")
    list_filter = ("category", )
    search_fields = ("title", "author__username")
    prepopulated_fields = {"slug": ("title", )}
    form = PostAdminForm
    save_as = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='50'>")
        else:
            return "-"

    get_image.short_description = "Изображение"


class CategoryAdmin(admin.ModelAdmin):
    """Категории"""

    prepopulated_fields = {"slug": ("name", )}


class TagAdmin(admin.ModelAdmin):
    """Теги"""

    prepopulated_fields = {"slug": ("name", )}


class LikeAdmin(admin.ModelAdmin):
    """Лайки"""

    list_display = ("post", "ip")


class CommentAdmin(admin.ModelAdmin):
    """Комментарии"""

    list_display = ("post", "author", "publish", "parent")
    search_fields = ("post__title", "author")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)