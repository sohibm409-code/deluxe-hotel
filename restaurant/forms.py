from datetime import date
from django import forms
from .models import TableReservation


class TableReservationForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = [
            'customer_name',
            'customer_phone',
            'customer_email',
            'reservation_date',
            'reservation_time',
            'guests',
            'special_requests',
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ismingiz (To\'liq)',
                'required': True,
            }),
            'customer_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqamingiz (+998...)',
                'required': True,
            }),
            'customer_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Elektron pochta (ixtiyoriy)',
            }),
            'reservation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True,
            }),
            'reservation_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tashrif vaqti (masalan: 19:30)',
                'required': True,
            }),
            'guests': forms.Select(
                choices=[
                    ('1 kishi', '1 kishi'),
                    ('2 kishi', '2 kishi (Romantik)'),
                    ('3-4 kishi', '3-4 kishi (Oila)'),
                    ('5-6 kishi', '5-6 kishi'),
                    ('7+ kishi', '7+ kishi (Katta davra)'),
                ],
                attrs={'class': 'form-control', 'required': True}
            ),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Qo\'shimcha istaklar (masalan, deraza yonidagi sokin stol, sham yorug\'i...)',
            }),
        }

    def clean_reservation_date(self):
        res_date = self.cleaned_data.get('reservation_date')
        if res_date and res_date < date.today():
            raise forms.ValidationError("O'tib ketgan sanaga stol band qilib bo'lmaydi.")
        return res_date
