from django.shortcuts import render
from django.views import generic
from .models import IrregularVerbs, Letter


def verb_list(request):
    # letter = Letter.objects.filter()

    context = {
        'letters': Letter.objects.all()
    }

    return render(request, 'verbs/home.html', context)    
