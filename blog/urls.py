from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', views.blog_detail_view, name="blog_detail"),
    path('<int:pk>/comment', views.blog_comment_view, name="blog_comment"),
    path('<int:pk>/comment/delete/', views.delete_blog_comment_view, name="blog_comment"),
]