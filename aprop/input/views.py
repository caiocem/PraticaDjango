from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from aprop.input.serializers import UserSerializer, GroupSerializer, ApropriacaoSerializer, ProjetoSerializer, ColaboradorSerializer
from aprop.input.models import Apropriacao, Projeto, Colaborador


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projeto.objects.all().order_by('-id')
    serializer_class = ProjetoSerializer


class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Colaborador.objects.all().order_by('-id')
    serializer_class = ColaboradorSerializer


class ApropriacaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Apropriacao.objects.all().order_by('-timestamp')
    serializer_class = ApropriacaoSerializer

# Create your views here.
