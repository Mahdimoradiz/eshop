from django.views.generic import DetailView
from blog.models import Blog, Category, BlogComment
from blog.forms import BlogCommentForm
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogView:
    model = Blog
    template_name = "blog/blog.html"
    

class BlogDetailView(LoginRequiredMixin, BlogView, DetailView, FormMixin):
    form_class = BlogCommentForm
    success_url = "/"  # Redirect to home after successful form submission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = self.get_object()
        comment_count = blog.blog_comments.count()
        context['comment_count'] = comment_count
        context['category'] = Category.objects.all()
        recent_posts = Blog.objects.exclude(pk=blog.pk).order_by('-create_at')[:3]
        context['recent_posts'] = recent_posts

        # Add new comment form
        
        new_comment = None
        if self.request.method == 'POST':
            comment_form = BlogCommentForm(data=self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.blog = blog
                new_comment.save()
        else:
            comment_form = BlogCommentForm()

        context['new_comment'] = new_comment
        context['comment_form'] = comment_form

        return context
