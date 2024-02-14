from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data['name']
        return f'*{name}*'

    class Meta:
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'time', 'people_number', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email',
                                             'data-rule': 'email', 'data-msg': 'Please enter a valid email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone',
                                            'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Time',
                                           'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}),
            'people_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'people',
                                                      'placeholder': '# of people', 'data-rule': 'minlen:1',
                                                      'data-msg': 'Please enter at least 1 chars'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'message'}),
        }

