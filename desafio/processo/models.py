from django.db import models
import csv

# Create your models here.

class Processos(models.Model):
    pasta = models.CharField(max_length=100),
    comarca = models.CharField(max_length=100),
    uf = models.CharField(max_length=100),
    
    def registrar_planilha(self):
        pasta = []
        comarca = []
        uf = []

        with open('processo/csv/processos.csv', 'r') as entrada:
            ler = csv.reader(entrada)
            next(ler)
            for linha in ler:
                pasta.append(linha[0][0:6])
                comarca.append(linha[0][6:-2])
                uf.append(linha[0][-2:])
    
        return pasta,comarca,uf