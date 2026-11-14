from django import forms
from datetime import date
from .models import Booking
from .utils import get_conflicting_booking

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'room' in self.fields:
            self.fields['room'].empty_label = "--- Xonani tanlang ---"

    class Meta:
        model = Booking
        fields = [
            'room', 'room_name', 'check_in', 'check_out', 
            'guests', 'customer_name', 'customer_phone', 'customer_email', 'notes'
        ]
        widgets = {
            'room': forms.Select(attrs={'class': 'form-select'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'customer_name': forms.TextInput(attrs={'placeholder': 'Ismingiz', 'required': True}),
            'customer_phone': forms.TextInput(attrs={'placeholder': 'Telefon raqamingiz', 'required': True}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'Email manzilingiz'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Qo\'shimcha istaklar...', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')
        room = cleaned_data.get('room')

        if check_in and check_out:
            if check_out <= check_in:
                raise forms.ValidationError("Ketish sanasi (Check-out) kelish sanasidan keyin bo'lishi kerak.")
            if check_in < date.today():
                raise forms.ValidationError("O'tib ketgan sanalarni tanlab bo'lmaydi.")

            if room:
                conflict = get_conflicting_booking(room, check_in, check_out, exclude_booking_id=self.instance.id if self.instance else None)
                if conflict:
                    raise forms.ValidationError(
                        f"Kechirasiz, '{room.title}' xonasi {conflict.check_in.strftime('%d.%m.%Y')} dan {conflict.check_out.strftime('%d.%m.%Y')} gacha allaqachon band qilingan! Iltimos, boshqa sanalarni yoki boshqa xonani tanlang."
                    )

        return cleaned_data
