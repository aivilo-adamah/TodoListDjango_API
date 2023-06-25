from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtilisateurViewSet,TacheViewSet

router = DefaultRouter()
router.register('utilisateurs', UtilisateurViewSet, basename='utilisateur')
router.register('taches', TacheViewSet, basename='tache')

urlpatterns = [
    path('', include(router.urls)),
]