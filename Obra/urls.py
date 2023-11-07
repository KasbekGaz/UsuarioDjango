from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ObraViewSet, GastoViewSet


router = DefaultRouter()
router.register(r'obras', ObraViewSet, basename='Obras-proyectos')
router.register(r'gastos', GastoViewSet, basename='GastosdeObra')


urlpatterns = [
    path('api/', include(router.urls))
]
