from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.urls import reverse

from .utilities import send_new_post_notification



class Category(models.Model):
    """Категории"""

    name = models.CharField(max_length=75, verbose_name="Название")
    slug = models.SlugField(max_length=75, verbose_name="URL", unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Теги"""

    name = models.CharField(max_length=75, verbose_name="Название")
    slug = models.SlugField(max_length=75, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Посты"""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(max_length=100, verbose_name="URL", unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts")
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги", related_name="posts")
    publish = models.DateTimeField(auto_now_add=True, verbose_name="Опубликован")
    update = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    is_draft = models.BooleanField(default=False, verbose_name="Черновик?")

    def __str__(self):
        return self.title
    
    def get_author_name(self):
        return self.author.username
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Activity(models.Model):
    """
    Лайки и просмотры статей
    """
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="activity")
    ip = models.GenericIPAddressField(verbose_name="IP")
    like = models.BooleanField(default=False, verbose_name="Лайк")

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Активность"
    

class Comment(models.Model):
    """Комментарии"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", related_name="comments")
    author = models.CharField(max_length=75, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст")
    publish = models.DateTimeField(auto_now_add=True, verbose_name="Опубликован")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Родитель", related_name="children")

    def __str__(self):
        return f"Комментарий {self.author} к {self.post}"

    def get_parent_comment_author(self):
        if self.parent:
            return self.parent.author

    def get_parent_comment_id(self):
        if self.parent:
            return self.parent.id

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["publish"]


class Contact(models.Model):
    """Подписка на рассылку по Email"""

    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


def post_save_dispatcher(sender, **kwargs):
    if kwargs['created']:
        send_new_post_notification(kwargs['instance'])


post_save.connect(post_save_dispatcher, sender=Post)