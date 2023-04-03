from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ecole, Reservation
from .forms import ReservationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def home(request):
    ecoles = Ecole.objects.all()
    return render(request, 'home.html', {'ecoles': ecoles})

@login_required
def reservation(request, ecole_id):
    ecole = get_object_or_404(Ecole, pk=ecole_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.ecole = ecole
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Votre réservation a été enregistrée.')
            return redirect('ecole', ecole_id=ecole_id)
    else:
        form = ReservationForm(initial={'client': request.user, 'ecole': ecole})
    return render(request, 'reservation.html', {'ecole': ecole, 'form': form})

@login_required
def ecole(request, ecole_id):
    ecole = get_object_or_404(Ecole, pk=ecole_id)
    reservations = Reservation.objects.filter(ecole=ecole)
    return render(request, 'ecole.html', {'ecole': ecole, 'reservations': reservations})

@login_required
def liste_reservations(request):
    reservations = Reservation.objects.filter(client=request.user)
    context = {'reservations': reservations}
    return render(request, 'liste_reservations.html', context)

@login_required
def annulation_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    ecole_id = reservation.ecole.pk
    if reservation.client != request.user:
        messages.error(request, 'Vous ne pouvez pas annuler cette réservation.')
        return redirect('ecole', ecole_id=ecole_id)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Votre réservation a été annulée.')
        return redirect('liste_reservations')

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})
