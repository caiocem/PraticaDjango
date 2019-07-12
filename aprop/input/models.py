from datetime import timedelta

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.

#  class Colaborador(models.Model):
#     email = models.EmailField(max_length=70,
#                               null=False,
#                               blank=False,
#                               unique=False)
#
#     def __str__(self):
#         return self.email
#
#     def get_absolute_url(self):
#         return reverse('colaborador_edit', kwargs={'pk': self.pk})


class Colaborador(User):
    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('colaborador_edit', kwargs={'pk': self.pk})


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    colaborador = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('projeto_edit', kwargs={'pk': self.pk})


class Apropriacao(models.Model):
    class Meta:
        verbose_name_plural = "Apropriações"

    timestamp = models.DateTimeField(auto_now_add=True)
    referencia = models.DateField()
    colaborador = models.ForeignKey(User, on_delete=models.PROTECT)
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    duracao = models.DurationField(validators=[
        MinValueValidator(timedelta(0)),
        MaxValueValidator(timedelta(hours=23, minutes=59))
    ])

    descricao = models.CharField(max_length=2048)

    def __str__(self):
        return str(self.referencia + self.colaborador.email +
                   self.projeto.nome)

    def get_absolute_url(self):
        return reverse('apropriacao_new', kwargs={'pk': self.pk})
