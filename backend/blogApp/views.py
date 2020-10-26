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
        posts = Post.objects.all()[count:count + 8]
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
    """Страница подробного представление поста"""

    def get(self, request, slug):
        post = Post.objects.get(slug__exact=slug)
        tags = Tag.objects.all()
        recent_posts = Post.objects.all().order_by('-publish')[:5]
        popular_posts = sorted(Post.objects.all(), key=lambda post: post.activity.count(), reverse=True)[:5]
        
        post_serializer = PostDetailSerializer(post)
        tags_seerializer = TagListSerializer(tags, many=True)
        recent_posts_serializer = PostListSerializer(recent_posts, many=True)
        popular_posts_serializer = PostListSerializer(popular_posts, many=True)

        return Response({
            "post": post_serializer.data,
            "tags": tags_seerializer.data,
            "recent_posts": recent_posts_serializer.data,
            "popular_posts": popular_posts_serializer.data,
        })


class CommentCreateView(APIView):
    """
    Добавление комментария
    """
    
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


class AddViewsAndLikesView(APIView):
    """
    Добавление лайков и просмторов
    """

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        activity = ActivityCreateSerializer(data=request.data)
        if activity.is_valid():
            activity.save(ip=self.get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


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