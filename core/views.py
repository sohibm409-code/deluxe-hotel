from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Blog
from rooms.models import Room
from .models import Service, Testimonial, HotelStat

class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blogs"] = Blog.objects.order_by("-created_at")[:4]
        context["rooms"] = Room.objects.filter(is_featured=True)[:6]
        context["services"] = Service.objects.filter(is_active=True)[:6]
        context["testimonials"] = Testimonial.objects.filter(is_active=True)[:6]
        context["stats"] = HotelStat.objects.filter(is_active=True)
        context["all_rooms"] = Room.objects.all()
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active=True)[:6]
        context["stats"] = HotelStat.objects.filter(is_active=True)
        context["all_rooms"] = Room.objects.all()
        return context
