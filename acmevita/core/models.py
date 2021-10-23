from django.db import models

'''
* Cada departamento deve possuir um *nome do departamento*.
* A API deve responder com uma listagem de departamentos no formato JSON informando o *nome do departamento* de cada departamento.

#### Como um Usuário da API eu gostaria de consultar todos os colaboradores de um departamento para visualizar a organização da ACMEVita.

* Cada colaborador deve possuir um *nome completo*.
* Cada colaborador deve pertencer a *um* departamento.
* Cada colaborador pode possuir *nenhum, um ou mais* dependententes.
* A API deve responder com uma listagem de colaboradores do departamento no formato JSON informando o *nome completo* de cada colaborador e
a respectiva flag booleana `have_dependents` caso o colaborador possua *um ou mais dependentes*.
'''

class Departamento(models.Model):
    departamento = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'departamento'

class Colaborador(models.Model):
    nome_completo = models.CharField(max_length=100,blank=False, null=False)
    id_departamento = models.ForeignKey(Departamento, related_name='colaboradores', on_delete=models.CASCADE, db_column='id_departamento')

    class Meta:
        db_table = 'colaborador'

class Dependente(models.Model):
    nome_completo = models.CharField(max_length=100,blank=False, null=False)
    id_colaborador = models.ForeignKey(Colaborador, related_name='dependentes', on_delete=models.CASCADE, db_column='id_colaborador')

    class Meta:
        db_table = 'dependente'
