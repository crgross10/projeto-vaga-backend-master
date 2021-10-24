from django.urls import path, include
from rest_framework import routers
from .views import (
      DepartamentoViewSet,
      ColaboradorViewSet,
      DependenteViewSet,
      DepartamentosViewSet,
      )


app_name = 'core'

router = routers.DefaultRouter()
router.register('departamento', DepartamentoViewSet)
router.register('colaborador', ColaboradorViewSet)
router.register('dependente', DependenteViewSet)
router.register('departamentos', DepartamentosViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
