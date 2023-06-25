from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Utilisateur(models.Model):
    SEXE_CATEGORY = (
        ('FEMININ', 'F'),
        ('MASCULIN', 'M'),
    )
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=8, choices=SEXE_CATEGORY, default='F')
    commentaire = models.TextField()
    Date_creation= models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tache(models.Model):
    STATUT_TACHE = (
        ('EN_COURS', 'En cours'),
        ('TERMINÉ', 'Terminé'),
        ('PAS_COMMENCÉ', 'Pas encore commencé')
    )
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField()
    commentaire = models.TextField(blank=True)
    statut = models.CharField(max_length=20, choices=STATUT_TACHE, default='PAS_COMMENCÉ')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)

    