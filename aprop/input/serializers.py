from django.contrib.auth.models import User, Group
from rest_framework import serializers
from aprop.input.models import Apropriacao, Projeto, Colaborador



class ApropriacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apropriacao
        fields = ('timestamp', 'referenciaApropriacao', 'colaborador', 'projeto', 'horas', 'descricao' )

class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projeto
        fields = ('nome')

class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = ('email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')