from django.contrib.auth.models import Group, User
from rest_framework import serializers

from aprop.input.models import Apropriacao, Colaborador, Projeto


class ApropriacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apropriacao
        fields = '__all__'


class ProjetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'


class ColaboradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
