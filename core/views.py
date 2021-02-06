from django.shortcuts import redirect, render

from core.models import Evento

# Create your views here.

def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    # usuario = request.user
    # eventos = Evento.objects.filter(usuario=usuario)
    eventos = Evento.objects.all()
    response = {'eventos': eventos}
    return render(request, 'agenda.html', response)
