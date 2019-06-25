from django.db import models

# Create your models here.


class Projeto(models.Model):
    nome = models.CharField(max_length=50)


class Colaborador(models.Model):
    email = models.EmailField(max_length=70, null=False, blank=False, unique=False)


class Apropriacao(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    referenciaApropriacao = models.DateTimeField()
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    horas = models.DurationField()
    descricao = models.CharField(max_length=2048)
