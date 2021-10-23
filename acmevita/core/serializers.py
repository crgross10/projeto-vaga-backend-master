from rest_framework import serializers
from .models import (
        Departamento,
        Colaborador,
        Dependente )



class ColaboradorSerializer(serializers.ModelSerializer):

    have_dependents = serializers.SerializerMethodField('get_dependentes')

    def get_dependentes(self, obj):
          dependentes = Dependente.objects.all()
          dependentes = dependentes.filter(id_colaborador=obj.id)
          if (dependentes):
              return True
          else:
              return False

    class Meta:
        model = Colaborador
        fields=('id','nome_completo', 'have_dependents')


class DependenteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dependente
        fields=('id','nome_completo','id_colaborador' )


class DepartamentoSerializer(serializers.ModelSerializer):

    colaboradores = ColaboradorSerializer(many=True, read_only=True)

    class Meta:
        model = Departamento
        fields=('id','departamento','colaboradores')
