from django.shortcuts import render
from django.views.generic import (DetailView, CreateView)
from blog.models import Blog
from blog.forms import BlogCommentForm

class BlogView:
    model = Blog
    template_name = "blog/blog.html"


class BlogDetailView(BlogView, DetailView):
    pass
    
class CreateBlogCommentView(BlogView, CreateView):
    form_class = BlogCommentForm
    success_url = "/"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
    
    