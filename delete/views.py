from django.shortcuts import render
from recordings.models import Summary,Recording_extend,Recording_rewrite
from django.shortcuts import render, redirect
import uuid
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def supprimer_enregistrement_ext(request):
    if request.method == 'POST':
        str_id = request.POST.get('idext')
        new_str_id = str_id.replace('/', '')
        record_id = uuid.UUID(new_str_id)
        record = Recording_extend.objects.get(id=record_id)
        record.delete()
        
        return redirect('toutenregistrement') 
    else:
        return redirect('toutenregistrement')  # Redirection si la méthode n'est pas POST
 
 
 
 
    
@csrf_exempt   
def delete_summary(request):
    if request.method == 'POST':
        str_id1 = request.POST.get('idsum')
        new_str_id1 = str_id1.replace('/', '')
        record_id1 = uuid.UUID(new_str_id1)
        record1 = Summary.objects.get(id=record_id1)
        record1.delete()
        
        return redirect('toutenregistrement') 
    else:
        return redirect('toutenregistrement')    
    
    
    
    
@csrf_exempt   
def delete_rewrite(request):
    if request.method == 'POST':
        str_id1 = request.POST.get('idrew')
        new_str_id1 = str_id1.replace('/', '')
        record_id1 = uuid.UUID(new_str_id1)
        record1 = Recording_rewrite.objects.get(id=record_id1)
        record1.delete()
        
        return redirect('toutenregistrement') 
    else:
        return redirect('toutenregistrement')    