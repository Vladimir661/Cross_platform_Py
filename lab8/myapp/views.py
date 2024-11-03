from django.shortcuts import render
from .models import Programmer, Error, Fix

def home(request):
    programmers = Programmer.objects.all()
    errors = Error.objects.all()
    fixes = Fix.objects.all()
    return render(request, 'home.html', {
        'programmers': programmers,
        'errors': errors,
        'fixes': fixes,
    })
