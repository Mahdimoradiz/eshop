from blog.models import Blog, Category
from blog.forms import BlogCommentForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    comment_count = blog.blog_comments.count()
    category = Category.objects.all()
    recent_posts = Blog.objects.exclude(pk=blog.pk).order_by('-create_at')[:3]
    context = {
        'blog': blog,
        'comment_count': comment_count,
        'category': category,
        'recent_posts': recent_posts,
    }
    return render(request, 'blog/blog.html', context)


@login_required
def blog_comment_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.author = request.user
            comment.save()
            return redirect('blog:blog_detail', pk=pk)
    else:
        form = BlogCommentForm()
    return render(request, 'blog/add_comment.html', {'blog': blog, 'form': form})


@login_required
def delete_blog_comment_view(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, 'Comment deleted')
        return redirect('blog:blog_detail', pk=pk)
    return render(request, 'blog/add_comment.html', {'comment': blog})
    



    
    # class BlogDetailView(DetailView):
    # model = Blog
    # template_name = "blog/blog.html"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     blog = self.get_object()
    #     comment_count = blog.blog_comments.count()
    #     context['comment_count'] = comment_count
    #     context['category'] = Category.objects.all()
    #     recent_posts = Blog.objects.exclude(pk=blog.pk).order_by('-create_at')[:3]
    #     context['recent_posts'] = recent_posts
    #     return context