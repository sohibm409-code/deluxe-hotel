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
