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


class CommentListSerializer(serializers.ModelSerializer):
    """Комментари к посту"""

    class Meta:
        model = Comment
        fields = ["author", "text", "publish"]
    

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