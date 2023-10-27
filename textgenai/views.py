from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from textgenai.helpers import *
import openai
import os
from recordings.models import Recording
from django.http import JsonResponse
from textgenai.serializer import *

key_openIA=openai.api_key=os.environ.get('OPENAI_API_KEY')

@api_view(['POST'])
def textgen(request):
    enter_question_serializer = EnterQuestionSerializer(data=request.data)
    if enter_question_serializer.is_valid():
        # chat gpt code            
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": enter_question_serializer.data["question"]}
        ]
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion.choices[0].message["content"]

        result = GenerateContentSerializer({"content": response}, many=False)
        print(result)
        return Response(result.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def extendgen(request):
    enter_extent_Content_Serializer= EnterextentContentSerializer(data=request.data)
    if enter_extent_Content_Serializer.is_valid():
        # chat gpt code 
        nombre=count_words(enter_extent_Content_Serializer.data['entertext']) 
        if( nombre>enter_extent_Content_Serializer.data['size']):     
            prompt = f"Rallongez le texte  suivant :{enter_extent_Content_Serializer.data['entertext']}avec une extenxion d'environ {enter_extent_Content_Serializer.data['size']} mots "
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
            extended_content = response["choices"][0]["message"]["content"]
            contenu=Recording(extended_content) 
            result = ExtentcontentSerializer({"extenttext":extended_content}, many=False)
            return Response(result.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'erreur': 'vous ne pouvez pas rallonger un texte en diaminuant la taille. bien vouloir modifier la taille entrée! '})
    else:
        return JsonResponse({'erreur': 'bien vouloir entrer un texte'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def summarygen(request):
    enter_resum_Content_Serializer= EnterresumeContentSerializer(data=request.data)
    if enter_resum_Content_Serializer.is_valid():
        # chat gpt code  
        nombre=count_words(enter_resum_Content_Serializer.data['resumetext']) 
        if (nombre<enter_resum_Content_Serializer.data['sizetext']):            
            prompt = prompt = f"Générez un résumé :\n{enter_resum_Content_Serializer.data['resumetext']}avec une extenxion d'environ{enter_resum_Content_Serializer.data['sizetext']}mots gardant ces mots inchangés{enter_resum_Content_Serializer.data['keyword']}"
            response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt}
                        ]
                    )
            text_resum= response["choices"][0]["message"]["content"]
            result = ExtentcontentSerializer({"extenttext":text_resum}, many=False)
            return Response(result.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'erreur': 'vous ne pouvez pas résumer un texte avec un nombre de supérieur à la taille du texte'})
    else:
        return JsonResponse({'erreur': 'bien vouloir entrer un texte'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def rewritegen(request):
    enter_extent_Content_Serializer= EnterrewriteContentSerializer(data=request.data)
    if enter_extent_Content_Serializer.is_valid():
        # chat gpt code               
        prompt = prompt = f"Réécrivez le texte suivant en préservant son idée générale :\n{enter_extent_Content_Serializer.data['entertext']}tout en gardant ces mots inchangés {enter_extent_Content_Serializer.data['keyword1']} "
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
        extended_content = response["choices"][0]["message"]["content"]
        result = ExtentcontentSerializer({"extenttext":extended_content}, many=False)
        
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'erreur': 'bien vouloir entrer un texte'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
