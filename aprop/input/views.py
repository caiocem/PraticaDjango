import django_tables2 as tables
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.contrib.auth import logout
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from django_tables2.utils import A  # alias for Accessor
from rest_framework import viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from aprop.input.forms import ApropriacaoForm
from aprop.input.models import Apropriacao, Colaborador, Projeto
from aprop.input.serializers import (ApropriacaoSerializer,
                                     ColaboradorSerializer, GroupSerializer,
                                     ProjetoSerializer, UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, )


class ProjetoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projeto.objects.all().order_by('-id')
    serializer_class = ProjetoSerializer
    permission_classes = (IsAuthenticated, )


class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Colaborador.objects.all().order_by('-id')
    serializer_class = ColaboradorSerializer
    permission_classes = (IsAuthenticated, )


class ApropriacaoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Apropriacao.objects.all().order_by('-timestamp')
    serializer_class = ApropriacaoSerializer
    permission_classes = (IsAuthenticated, )


class ApropriacaoTable(tables.Table):
    edit = tables.LinkColumn('apropriacao_edit', text='Editar', args=[A('pk')])
    view = tables.LinkColumn('apropriacao_view',
                             text='Ver detalhes',
                             args=[A('pk')])
    delete = tables.LinkColumn('apropriacao_delete',
                               text='Remover',
                               args=[A('pk')])

    class Meta:
        model = Apropriacao
        exclude = ['id', 'timestamp']


class ApropriacaoList(SingleTableView):
    model = Apropriacao
    table_class = ApropriacaoTable
    table_data = Apropriacao.objects.filter(colaborador=1)


#    permission_classes = (IsAuthenticated)


class ApropriacaoView(DetailView):
    model = Apropriacao


#    permission_classes = (IsAuthenticated)


class GetFormMock():
    def get_form(self):
        form = super().get_form()
        form.fields['referenciaApropriacao'].widget = DatePickerInput(
            attrs={'placeholder': 'Selecione uma data'})
        form.fields['horas'].widget = TimePickerInput(
            attrs={'placeholder': '8:00'})
        return form


class ApropriacaoCreate(CreateView, GetFormMock):
    model = Apropriacao
    form = ApropriacaoForm()
    fields = [
        'referenciaApropriacao', 'colaborador', 'projeto', 'horas', 'descricao'
    ]
    success_url = reverse_lazy('apropriacao_list')


class ApropriacaoUpdate(UpdateView, GetFormMock):
    model = Apropriacao
    fields = [
        'referenciaApropriacao', 'colaborador', 'projeto', 'horas', 'descricao'
    ]
    success_url = reverse_lazy('apropriacao_list')


class ApropriacaoDelete(DeleteView):
    model = Apropriacao
    success_url = reverse_lazy('apropriacao_list')
