from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Contact
from .forms import ContactForm

class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:index')
    success_message = "Xabaringiz muvaffaqiyatli yuborildi! Tez orada siz bilan bog'lanamiz."

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            from core.telegram import notify_telegram
            c = self.object
            notify_telegram(
                f"📩 <b>Yangi Xabar (Aloqa bo'limidan)!</b>\n\n"
                f"👤 <b>Ism:</b> {c.full_name}\n"
                f"📞 <b>Telefon:</b> {c.phone}\n"
                f"📧 <b>Email:</b> {c.email}\n"
                f"📝 <b>Mavzu:</b> {c.subject}\n"
                f"💬 <b>Xabar matni:</b>\n{c.description}"
            )
        except Exception:
            pass
        return response
