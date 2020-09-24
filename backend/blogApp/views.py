from rest_framework.response import Response 
from rest_framework.views import APIView


from blogApp.models import *
from blogApp.serializers import *


class MainView(APIView):
    """Начальная страница"""

    def get(self, request):
        posts = Post.objects.all()[:8]
        categories = Category.objects.all()
        posts_serializer = PostListSerializer(posts, many=True)
        categories_serializer = CategorySerializer(categories, many=True)
        return Response({
            "posts": posts_serializer.data,
            "categories": categories_serializer.data,
        })


class PostDetailView(APIView):
    """Подробное представление поста"""

    def get(self, request, slug):
        post = Post.objects.get(slug__exact=slug)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostsByCategoryView(APIView):
    """Список постов относящихся к оперделенной категории"""

    def get(self, request, slug):
        posts = Post.objects.filter(category__slug=slug)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostsByTagView(APIView):
    """Список фильмов относящихся к определённому тегу"""

    def get(self, request, slug):
        posts = Post.objects.filter(tags__slug=slug)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)