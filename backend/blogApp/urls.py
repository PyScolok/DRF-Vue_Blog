from django.urls import path
from blogApp.views import *

urlpatterns = [
    path("main/", MainView.as_view()),
    path("post/<str:slug>/", PostDetailView.as_view()),
    path("add_comment/", CommentCreateView.as_view()),
    path("add_view/", AddViewsAndLikesView.as_view()),
    path("add_subscriber/", AddSubscriberView.as_view()),
    path("categories/", CategoriesListView.as_view()),
    path("category/<str:slug>/", PostsByCategoryView.as_view()),
    path("tag/<str:slug>/", PostsByTagView.as_view()),
]