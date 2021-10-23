from django.urls import path, include
from rest_framework import routers
from .views import (
      DepartamentoViewSet,
      ColaboradorViewSet,
      DependenteViewSet
      )


app_name = 'core'

router = routers.DefaultRouter()
router.register('departamento', DepartamentoViewSet)
router.register('colaborador', ColaboradorViewSet)
router.register('dependente', DependenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
