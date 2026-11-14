from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Room

class RoomsView(ListView):
    model = Room
    template_name = "rooms/rooms.html"
    context_object_name = "rooms"
    paginate_by = 9

    def get_queryset(self):
        queryset = Room.objects.all()
        q = self.request.GET.get("q")
        room_type = self.request.GET.get("room_type")
        adults = self.request.GET.get("adults")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(view__icontains=q))
        if room_type and room_type != "Room Type":
            queryset = queryset.filter(title__icontains=room_type)
        if adults and adults != "0 Adult":
            # Extract number e.g. "3 Adult" -> 3
            try:
                num = int(adults.split()[0])
                queryset = queryset.filter(max_persons__gte=num)
            except (ValueError, IndexError):
                pass
        if min_price:
            try:
                queryset = queryset.filter(price__gte=float(min_price))
            except ValueError:
                pass
        if max_price:
            try:
                queryset = queryset.filter(price__lte=float(max_price))
            except ValueError:
                pass

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_room_types"] = Room.objects.values_list("title", flat=True).distinct()
        return context

class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room-detail.html"
    context_object_name = "room"
