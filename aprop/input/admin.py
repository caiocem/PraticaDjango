from django.contrib import admin


# Register your models here.
from django.contrib import admin

from aprop.input.models import Apropriacao, Colaborador, Projeto
admin.site.register(Apropriacao)
admin.site.register(Colaborador)
admin.site.register(Projeto)
