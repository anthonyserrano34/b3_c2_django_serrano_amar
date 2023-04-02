from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ecole, Reservation

def home(request):
    ecoles = Ecole.objects.all()

@login_required
def reservation(request, ecole_id):
    ecole = get_object_or_404(Ecole, pk=ecole_id)

@login_required
def ecole(request, ecole_id):
    ecole = get_object_or_404(Ecole, pk=ecole_id)
    reservations = Reservation.objects.filter(ecole=ecole)

@login_required
def annulation_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    ecole_id = reservation.ecole.pk
    if reservation.user != request.user:
        messages.error(request, 'Vous ne pouvez pas annuler cette réservation.')
        return redirect('ecole', ecole_id=ecole_id)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Votre réservation a été annulée.')
        return redirect('ecole', ecole_id=ecole_id)
