from rest_framework.response import Response 
from rest_framework.views import APIView


from blogApp.models import *
from blogApp.serializers import *


class MainView(APIView):
    """Начальная страница"""

    def get(self, request):
        if request.GET.get('count'):
            count = int(request.GET.get('count'))
        else:
            count = 0
        posts = Post.objects.all()[count:count + 4]
        posts_serializer = PostListSerializer(posts, many=True)
        return Response({
            "posts": posts_serializer.data,
        })


class CategoriesListView(APIView):
    """Список категорий"""

    def get(self, request):
        categories = Category.objects.all()
        categories_serializer = CategoryListSerializer(categories, many=True)
        return Response({
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