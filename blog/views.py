from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Blog, BlogComment

class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html' 
    context_object_name = "blogs"
    ordering = ['-created_at']
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        cat = self.request.GET.get('category')
        if cat:
            queryset = queryset.filter(category=cat)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Blog.CATEGORY_CHOICES
        context["selected_cat"] = self.request.GET.get('category', '')
        return context
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog-single.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blogs"] = Blog.objects.exclude(pk=self.object.pk).order_by('-created_at')[:3]
        context["comments"] = self.object.comments.filter(is_approved=True)
        context["categories"] = Blog.CATEGORY_CHOICES
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        comment_text = request.POST.get('comment', '').strip()

        if name and email and comment_text:
            BlogComment.objects.create(
                blog=self.object,
                name=name,
                email=email,
                comment=comment_text,
                is_approved=True
            )
            messages.success(request, "Fikringiz muvaffaqiyatli qoldirildi! Fikringiz uchun tashakkur.")
        else:
            messages.error(request, "Iltimos, barcha majburiy maydonlarni to'ldiring.")

        return redirect('blog:blog_detail', pk=self.object.pk)

