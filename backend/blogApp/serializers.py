from rest_framework import serializers

from blogApp.models import *


class PostListSerializer(serializers.ModelSerializer):
    """Список постов"""

    author = serializers.CharField(source="get_author_name")

    class Meta:
        model = Post
        exclude = ["category", "tags", "is_draft", ]


class CategoryListSerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = "__all__"


class TagListSerializer(serializers.ModelSerializer):
    """Список тегов"""

    class Meta:
        model = Tag
        fields = "__all__"


class RecursiveChildrenSerializer(serializers.Serializer):
    """
    Рекурсивный вывод вложенных комментариев    
    """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterCommentListSerializer(serializers.ListSerializer):
    """
    Фильтрация комментов по наличию родителя
    """
    
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class CommentListSerializer(serializers.ModelSerializer):
    """Комментари к посту"""

    children = RecursiveChildrenSerializer(many=True)
    parent = serializers.CharField(source="get_parent_comment_author")


    class Meta:
        list_serializer_class = FilterCommentListSerializer 
        model = Comment
        fields = ["author", "text", "publish", 'children', 'parent']
    

class LikeListSerializer(serializers.ModelSerializer):
    """Лайки к посту"""

    class Meta:
        model = Like
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    """Пост"""

    author = serializers.CharField(source="get_author_name")
    category = CategoryListSerializer()
    tags = TagListSerializer(many=True)
    comments = CommentListSerializer(many=True)
    likes = LikeListSerializer(many=True)

    class Meta:
        model = Post
        exclude = ["is_draft", ]