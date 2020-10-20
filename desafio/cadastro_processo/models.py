from django.db import models

# Create your models here.

class Planilha(models.Model):
    nome = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='processo/csv/', null=True, blank=True)

    def __str__(self):
        return self.nome


                
