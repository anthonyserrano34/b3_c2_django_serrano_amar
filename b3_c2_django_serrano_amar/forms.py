from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Reservation, Ecole

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['ecole']
        fields = ['client', 'date']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker'}),
        }

class EcoleForm(forms.ModelForm):
    class Meta:
        model = Ecole
        fields = ['nom', 'adresse']

class LoginForm(AuthenticationForm):
    pass

class AnnulationReservationForm(forms.Form):
    confirmation = forms.BooleanField()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
