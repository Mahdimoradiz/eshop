from django.views.generic import DetailView
from blog.models import Blog, Category
from blog.forms import BlogCommentForm
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from django.views.generic.edit import CreateView


class BlogView:
    model = Blog
    template_name = "blog/blog.html"


class BlogDetailView(BlogView, DetailView, FormMixin):
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
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object  # Associate comment with the current blog post
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.blog_comments = self.get_object()  # Associate comment with the current blog post
            obj.save()
        else:
            return redirect("/")
        return super().form_valid(form)


