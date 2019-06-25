# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from aprop.input.models import Apropriacao, Colaborador, Projeto
from aprop.input.resourses import (ApropriacaoResource, ColaboradorResource,
                                   ProjetoResource)


class ProjetoAdmin(ImportExportModelAdmin):
    resource_class = ProjetoResource


class ApropriacaoAdmin(ImportExportModelAdmin):
    resource_class = ApropriacaoResource


class ColaboradorAdmin(ImportExportModelAdmin):
    resource_class = ColaboradorResource


admin.site.register(Apropriacao, ApropriacaoAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Projeto, ProjetoAdmin)
