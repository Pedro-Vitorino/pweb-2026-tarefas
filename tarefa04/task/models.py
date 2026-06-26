from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField(verbose_name="Finalizado?")
    prazo = models.DateField()

    def __str__(self):
        return self.nome
