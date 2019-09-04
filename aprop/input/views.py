import datetime

import django_tables2 as tables
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
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
    class Meta:
        model = Apropriacao
        exclude = ['id', 'timestamp', 'colaborador']


class ApropriacaoList(LoginRequiredMixin, SingleTableView):
    model = Apropriacao
    table_class = ApropriacaoTable

    def get_queryset(self):
        qs = self.model.objects.filter(colaborador=self.request.user)
        return qs


class ApropriacaoView(LoginRequiredMixin, ExportMixin, DetailView):
    model = Apropriacao


class ApropriacaoCreate(LoginRequiredMixin, ExportMixin, CreateView,
                        SingleTableView):
    model = Apropriacao

    form = ApropriacaoForm()
    fields = ['referencia', 'projeto', 'duracao', 'descricao']
    success_url = reverse_lazy('apropriacao_new')
    table_class = ApropriacaoTable
    login_url = "/social/login"

    # FIXME - Hack para funcionar apos uma inserção
    table = Apropriacao.objects.none()
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
            format='%Y-%m-%d',
            attrs={'placeholder': date.isoformat()},
        )
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
