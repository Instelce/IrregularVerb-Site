from django.shortcuts import render
from django.views import generic
from .models import IrregularVerbs, Letter, Fiche


def verb_list(request):
    context = {
        'letters': Letter.objects.all(),
        'fiches': Fiche.objects.get()
    }

    return render(request, 'verbs/home.html', context)    
