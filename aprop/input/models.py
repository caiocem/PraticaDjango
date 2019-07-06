from django.db import models
from django.urls import reverse

# Create your models here.


class Colaborador(models.Model):
    email = models.EmailField(max_length=70,
                              null=False,
                              blank=False,
                              unique=False)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('colaborador_edit', kwargs={'pk': self.pk})


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('projeto_edit', kwargs={'pk': self.pk})


class Apropriacao(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    referenciaApropriacao = models.DateField()
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    horas = models.DurationField()
    descricao = models.CharField(max_length=2048)

    def __str__(self):
        return str(self.referenciaApropriacao)

    def get_absolute_url(self):
        return reverse('apropriacao_edit', kwargs={'pk': self.pk})
