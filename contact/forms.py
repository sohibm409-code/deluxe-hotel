from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'phone', 'description']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'Write your message here...', 'required': True}),
        }
