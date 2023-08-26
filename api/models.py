from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    tempo_experiencia = models.CharField(max_length=255)
    linguagem_favorita = models.CharField(max_length=255)

    def __str__(self):
        return f'nome: {self.nome}, linguagem favorita: {self.linguagem_favorita}'