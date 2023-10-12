from django.shortcuts import render

# Create your views here.
from recordings.models import Summary, Recording_extend, Recording_rewrite
from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def affichage(request):
    summ = Summary.objects.filter(utilisateur=request.user)
    enregistrements_Recording_extend = Recording_extend.objects.filter(utilisateur=request.user)
    enregistrements_Recording_rewrite =  Recording_rewrite.objects.filter(utilisateur=request.user)
    
    context = {
        'summ': summ,
        'enregistrements_Recording_extend': enregistrements_Recording_extend,
        'enregistrements_Recording_rewrite': enregistrements_Recording_rewrite
    }

    return render(request, 'enregistrements.html', context)
