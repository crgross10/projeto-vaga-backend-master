from django.shortcuts import render
from rest_framework import viewsets

from .models import (
        Departamento,
        Colaborador,
        Dependente )

from .serializers import (
        DepartamentoSerializer,
        ColaboradorSerializer,
        DependenteSerializer,
        DepartamentosSerializer)


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class =  DepartamentoSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class =  ColaboradorSerializer

class DependenteViewSet(viewsets.ModelViewSet):
    queryset = Dependente.objects.all()
    serializer_class =  DependenteSerializer


class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class =  DepartamentosSerializer
