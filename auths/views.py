from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# from django.contrib.auth.models import User
from auths.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def logine(request):
    if request.method == 'POST':
        email = request.POST.get('email',False)
        password = request.POST.get('password',False)
        if email and password:
            user = authenticate(request,username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                text = "Email ou mot de passe incorrect !"
                context = {'text': text,'email': email,'password': password}
                return render(request, 'login.html', context)
        else:
            text = "Veuillez remplir tous les champs !"
            context = {'text': text,'email': email,'password': password}
            return render(request, 'login.html', context)

    return render(request, 'login.html')
    
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')

        if firstname and lastname and email and password1:
            
            if password1 != password2:
                reponse="les mots de passe sont différents!"
                context={'reponse':reponse,'firstname': firstname,'lastname': lastname,'email': email,'password1': password1,'password2': password2 }
                return render (request, 'signup.html', context)
            # Vérifier si l'email existe déjà
            if User.objects.filter(email=email).exists():
                text=" Cette email existe déjà!"
                context={'text':text,'firstname': firstname,'lastname': lastname,'email': email,'password1': password1,'password2': password2 }
                return render (request, 'signup.html', context)

            try:
                my_user, created = User.objects.get_or_create(username=firstname, email=email, last_name=lastname)
                my_user.set_password(password1)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                text2="Un compte avec le même nom d'utilisateur existe déjà !!"
                context={'text2':text2,'firstname': firstname,'lastname': lastname,'email': email,'password1': password1,'password2': password2 }
                return render (request, 'signup.html', context)
        else:
             text1="Bien vouloir remplir tous les champs!"
             context={'text1':text1,'firstname': firstname,'lastname': lastname,'email': email,'password1': password1,'password2': password2 }
             return render (request, 'signup.html', context)

    return render(request, 'signup.html')



def mpd(request):
    if request.method == 'POST':
        email = request.POST['email']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            error_message = "L'utilisateur avec cette adresse e-mail n'existe pas."
            context = {'error_message1': error_message,'email': email,'new_password': new_password,'confirm_password': confirm_password}
            return render(request, 'mpd.html', context)

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            success_message = "Votre mot de passe a été réinitialisé avec succès."
            context = {'success_message': success_message,'email': email,'new_password': new_password,'confirm_password': confirm_password}
            return render(request, 'mpd.html', context)
        else:
            error_message = "Les mots de passe ne correspondent pas."
            context = {'error_message2': error_message,'email': email,'new_password': new_password,'confirm_password': confirm_password}
            return render(request, 'mpd.html', context)

    return render(request, 'mpd.html')

def deconnexion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')