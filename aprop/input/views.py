import datetime

import django_tables2 as tables
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.contrib.auth import logout
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
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
    #    edit = tables.LinkColumn('apropriacao_edit',
    # text='Editar', args=[A('pk')])
    #    view = tables.LinkColumn('apropriacao_view',
    #                             text='Ver detalhes',
    #                             args=[A('pk')])
    #    delete = tables.LinkColumn('apropriacao_delete',
    #                               text='Remover',
    #                               args=[A('pk')])

    class Meta:
        model = Apropriacao
        exclude = ['id', 'timestamp']


class ApropriacaoList(LoginRequiredMixin, SingleTableView):
    model = Apropriacao
    table_class = ApropriacaoTable

    def get_queryset(self):
        qs = self.model.objects.filter(colaborador=self.request.user)
        return qs


#    permission_classes = (IsAuthenticated)


class ApropriacaoView(LoginRequiredMixin, DetailView):
    model = Apropriacao


#    permission_classes = (IsAuthenticated)


class ApropriacaoCreate(LoginRequiredMixin, CreateView, SingleTableView):
    model = Apropriacao

    form = ApropriacaoForm()
    fields = ['referencia', 'projeto', 'duracao', 'descricao']
    success_url = reverse_lazy('apropriacao_new')
    table_class = ApropriacaoTable

    # FIXME - Hack para funcionar apos uma inserçãoõ
    table = Apropriacao.objects.all()
    object_list = table

    def get_queryset(self):
        qs = self.model.objects.filter(
            colaborador=self.request.user).order_by('-referencia')
        return qs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.colaborador = self.request.user
        self.object.save()
        return super(CreateView, self).form_valid(form)

    def get_form(self):
        date = datetime.datetime.now().date()

        form = super().get_form()
        generico = Projeto.objects.filter(nome="Genérico").get().pk
        form.fields['projeto'].initial = generico
        form.fields['referencia'].widget = DatePickerInput(
            format='%d/%m/%Y',
            attrs={
                'placeholder':
                str(date.day) + "/" + str(date.month) + "/" + str(date.year)
            },
            options={
                "showClose":
                True,
                "showClear":
                False,
                "showTodayButton":
                True,
                "defaultDate":
                str(date.day) + "/" + str(date.month) + "/" + str(date.year)
            })
        form.fields['referencia'].initial = str(date.day) + "/" + str(
            date.month) + "/" + str(date.year)
        form.fields['duracao'].widget = TimePickerInput(
            format='%H:%M',
            attrs={'placeholder': '08:00'},
            options={
                "showClose": True,
                "showClear": False,
                "showTodayButton": False,
                "stepping": 5,
            })
        form.fields['duracao'].initial = "08:00"
        return form


class ApropriacaoUpdate(LoginRequiredMixin, UpdateView, SingleTableView):
    model = Apropriacao
    fields = ['referencia', 'projeto', 'duracao', 'descricao']
    success_url = reverse_lazy('apropriacao_list')
    table_class = ApropriacaoTable
    table = Apropriacao.objects.filter(colaborador=1)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.colaborador = self.request.user
        self.object.save()
        return super(UpdateView, self).form_valid(form)

    def get_form(self):
        date = datetime.datetime.now().date()

        form = super().get_form()
        form.fields['referencia'].widget = DatePickerInput(
            format='%d/%m/%Y',
            attrs={
                'placeholder':
                str(date.year) + "/" + str(date.month) + "/" + str(date.day)
            })
        form.fields['duracao'].widget = TimePickerInput(
            format="%H:%M", attrs={'placeholder': '08:00'})
        return form


class ApropriacaoDelete(LoginRequiredMixin, DeleteView):
    model = Apropriacao
    success_url = reverse_lazy('apropriacao_list')
