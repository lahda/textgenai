from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import JsonResponse
import openai
from django.http import FileResponse
from django.views import View
from spinner.help import *


key_openIA=openai.api_key = "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"


#this function allows for generating content
def chat_completion(request):
    if request.method == 'POST':
        questions = request.POST.get('questions')  # Récupère la question de l'utilisateur depuis la requête GET
        
        if questions:
            prompt = f"voici ma question :\n{questions}"
            openai.api_key = key_openIA
            engine_list = openai.Engine.list() 
            response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                             {"role": "user", "content": prompt}
                            ]
                            )

            reponse = response["choices"][0]["message"]["content"]
            context={'reponse':reponse,'questions':questions}
            return render (request, 'dashboardGEn.html', context)
        else:
            text3gn='Posez votre question!'
            context1={'text3gn':text3gn,'questions':questions }
            return render(request, 'dashboardGEn.html',context1)
    else:
        
        return render(request, 'dashboardGEn.html',context={'text4':''})

@csrf_exempt
def generate_summary(request):
   
    if request.method == 'POST':
        
        input_text = request.POST.get('texteoriginalres', '')
        size_of_the_text = request.POST.get('size_of_the_text')
        additional_words = request.POST.get('additional_words')
        
        if input_text and size_of_the_text and additional_words:
            
            word_count1 = count_words(input_text)
            print(word_count1)# Appel à la fonction count_words avec le texte extrait du PDF
            tldr_tag = "\n tl;dr:"
        
            prompt = f"résume ce:\n{input_text}exactement en {size_of_the_text}mots. en gardant ces mots{additional_words}"
            openai.api_key = key_openIA
            engine_list = openai.Engine.list()
            size_of_the_text2 =int(size_of_the_text)
            word_count2 = int(word_count1)
            
            if word_count2 > 3000:
               
                # return JsonResponse({'error': 'Le nombre de mots est supérieur à 3000. Veuillez réduire la taille du texte.'})
                text = 'Le nombre de mots est supérieur à 3000. Veuillez réduire le  texte.'
                return render(request, 'dashboardRESum.html', context={"are":text,'keywords':additional_words,'taille':size_of_the_text, 'textoriginale':input_text})
            else:
                
                if word_count2>size_of_the_text2:
                   
                    response = openai.ChatCompletion.create(
                                        model="gpt-3.5-turbo",
                                        messages=[
                                            {"role": "user", "content": prompt}
                                        ]
                                    )

                    summary = response["choices"][0]["message"]["content"]
                    No=count_words(summary)
                    
                    print(No)
                    
                    context={'summary':summary, 'textoriginale':input_text,'keywords':additional_words,'taille':size_of_the_text}
                    return render (request, 'dashboardRESum.html', context)
                #JsonResponse({'summary': summary})
                else:
                    
                    text1='Le nombre de mot du texte original est plus petit que le nombre de mot entré, bien vouloir réduire le nombre de mot que vous entrez!'
                    context1={'text1re':text1,'textoriginale':input_text,'keywords':additional_words,'taille':size_of_the_text}
                    return render(request, 'dashboardRESum.html',context1)
        else:
           
            text3='Bien vouloir remplir tous les champs!'
            context2={'text3re':text3,'textoriginale':input_text,'keywords':additional_words,'taille':size_of_the_text}
            return render(request , 'dashboardRESum.html',context2 )
    return render(request, 'dashboardRESum.html',context={'text4':''})


@csrf_exempt
def generate_rewrite(request):
    if request.method == 'POST':
        input_text = request.POST.get('texteoriginalrec')
        additional_words = request.POST.get('keywords1')  # Récupération des mots supplémentaires entrés par l'utilisateur
        
        if input_text and additional_words:
            word_count1 = count_words(input_text)  # Appel à la fonction count_words avec le texte extrait du PDF
            word_count2 = int(word_count1)
            tldr_tag = "\n tl;dr:"
            prompt = f"paraphrase ce texte:\n{input_text}en gardant ces mot {additional_words} "
              
            openai.api_key = key_openIA
            engine_list = openai.Engine.list()

            if word_count2 >3000:
                text = 'Le nombre de mots est supérieur à 3000. Veuillez réduire la taille du texte.'
                return render(request, 'dashbord.html', context={"ar":text,'textoriginale':input_text ,'keywords':additional_words} )
            else:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                rewrite = response["choices"][0]["message"]["content"]
                print('tototo rewrite: {}'.format(rewrite))
                context={'rewrite':rewrite,'textoriginale':input_text ,'keywords':additional_words }
                return render (request, 'dashbord.html', context)
        else:
            text3='Bien vouloir remplir tous les champs!'
            return render(request , 'dashbord.html', context={'text3r':text3,'textoriginale':input_text ,'keywords':additional_words})

    return  render(request, 'dashbord.html',context={'text4':''})



@csrf_exempt
def extend_content(request):
    if request.method == 'POST':
        input_text2= request.POST.get('texteoriginal')
        size_of_the_text = request.POST.get('text_size2')
    
        if input_text2 and size_of_the_text:
            word_count1 = count_words(input_text2)# Appel à la fonction count_words avec le texte extrait du PDF
            size_of_the_text1 =int(size_of_the_text)
            word_count2 = int(word_count1)
            
            if word_count2 > 2000:
               
                # return JsonResponse({'error': 'Le nombre de mots est supérieur à 3000. Veuillez réduire la taille du texte.'})
                text = 'Le nombre de mots est supérieur à 2000. Veuillez réduire la taille du texte.'
                return render(request, 'mytemplate.html', context={"a":text,'textoriginale':input_text2,'taille':size_of_the_text})
            else:
                
                if size_of_the_text1 > word_count2:
                        tldr_tag = "\n tl;dr:"
                        
                        openai.api_key = key_openIA
                        prompt = f"Rallonge ce:\n{input_text2}exactement en {size_of_the_text}mots;  "
            

                        response = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                                {"role": "user", "content": prompt}
                            ]
                        )

                        extendeContent = response["choices"][0]["message"]["content"]
                        word=count_words(extendeContent)
                        print(word)      
                        context={'extendeContent':extendeContent,'textoriginale':input_text2,'taille':size_of_the_text }
                        return render (request, 'dashboardRall.html', context)
                else: 
                       text1='Le nombre de mot que vous avez entré  est inférieur à au nombre de mot du texte, bien vouloir augmenter  le nombre de mot.'
                       context1={'text1':text1,'textoriginale':input_text2,'taille':size_of_the_text}
                       return render(request, 'dashboardRall.html',context1)
        else:
            text3='Bien vouloir remplir tous les champs!'
            return render(request , 'dashboardRall.html', context={'text3':text3,'textoriginale':input_text2,'taille':size_of_the_text})
    return render(request, 'dashboardRall.html',context={'text4':''})



def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')

