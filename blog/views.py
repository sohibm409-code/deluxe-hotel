from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html' 
    context_object_name = "blogs"
    ordering = ['-created_at']
    paginate_by = 6
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog-single.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blogs"] = Blog.objects.exclude(pk=self.object.pk).order_by('-created_at')[:3]
        return context
