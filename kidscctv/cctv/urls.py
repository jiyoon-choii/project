from django.urls import path
from . import views

urlpatterns = [
    path('article/main',views.article_main, name="article/main"),
    # path('article/insert_all',views.article_insert_all, name="article/insert_all")
]