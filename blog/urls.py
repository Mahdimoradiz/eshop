from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
    path('', views.CreateBlogCommentView.as_view(), name="create_blog_comment"),
    
]