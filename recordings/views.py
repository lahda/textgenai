from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from recordings.models import Summary,Recording_extend,Recording_rewrite
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
@csrf_exempt
def sauvegarder_contenu_rewrite(request):
    if request.method == 'POST':
        titre = request.POST.get('title')
        contenu = request.POST.get('content')
        
        print('tototo contenu: {}'.format(contenu))
        if contenu and titre:
            # Création et sauvegarde de l'instance du modèle Contenu
            
            contenu_obj = Recording_rewrite(titre=titre, contenu=contenu, utilisateur=request.user)
            contenu_obj.save()
            return redirect('toutenregistrement')
        else:
            # Enregistrement échoué, affichage du message d'erreur
            messages.error(request, 'Impossible d\'enregistrer. Veuillez remplir tous les champs.')
    
    return redirect('toutenregistrement')
   

@login_required
@csrf_exempt
def sauvegarder_contenu_extends(request):
    if request.method == 'POST':
        titre = request.POST.get('title')
        contenu = request.POST.get('content')
        if contenu and titre:
        # Création et sauvegarde de l'instance du modèle Contenu
            contenu_obj = Recording_extend(titre=titre, contenu=contenu, utilisateur=request.user)
            contenu_obj.save()
            return redirect('toutenregistrement')
        
@login_required    
@csrf_exempt
def sauvegarder_contenu_summary(request):
    if request.method == 'POST':
        titre = request.POST.get('title')
        contenu = request.POST.get('content')

        # Création et sauvegarde de l'instance du modèle Contenu
        if contenu and titre:
            contenu_obj = Summary(titre=titre, contenu=contenu, utilisateur=request.user)
            contenu_obj.save()

            return redirect('toutenregistrement')


    