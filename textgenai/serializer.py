from rest_framework import serializers

# création d'une classe serializer
class EnterQuestionSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=255)
    
class GenerateContentSerializer(serializers.Serializer):
    content = serializers.CharField()
    
class EnterextentContentSerializer(serializers.Serializer):
    entertext= serializers.CharField(max_length=1000)
    size= serializers.ListField(child=serializers.CharField())
    
    
class EnterrewriteContentSerializer(serializers.Serializer):
    entertext= serializers.CharField(max_length=3000)
    keyword1= serializers.IntegerField()    
    
class ExtentcontentSerializer(serializers.Serializer):
    extenttext= serializers.CharField()  
         
class EnterresumeContentSerializer(serializers.Serializer):
    resumetext= serializers.CharField(max_length=3000)
    sizetext= serializers.IntegerField() 
    keyword = serializers.ListField(child=serializers.CharField())    