import uuid
from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Summary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    titre = models.CharField(default="", max_length=255)
    contenu = models.TextField()
    date = models.DateField(auto_now=True)
    
class Recording_extend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    titre = models.CharField(default="", max_length=255)
    contenu = models.TextField()
    date = models.DateField(auto_now=True)
       
class Recording_rewrite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    titre = models.CharField(default="", max_length=255)
    contenu = models.TextField()
    date = models.DateField(auto_now=True)
    