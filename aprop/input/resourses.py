from import_export import resources

from .models import Apropriacao, Colaborador, Projeto


class ProjetoResource(resources.ModelResource):
    class Meta:
        model = Projeto


class ColaboradorResource(resources.ModelResource):
    class Meta:
        model = Colaborador


class ApropriacaoResource(resources.ModelResource):
    class Meta:
        model = Apropriacao
