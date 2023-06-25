from rest_framework import viewsets

from .models import Utilisateur, Tache
from .serializers import UtilisateurSerializer, TacheSerializer


class UtilisateurViewSet(viewsets.ModelViewSet):
    serializer_class = UtilisateurSerializer
    queryset =Utilisateur.objects.all()

class TacheViewSet(viewsets.ModelViewSet):
    serializer_class = TacheSerializer
    queryset = Tache.objects.all()