# Generated by Django 4.2.2 on 2023-06-25 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('sexe', models.CharField(choices=[('FEMININ', 'F'), ('MASCULIN', 'M')], default='F', max_length=8)),
                ('commentaire', models.TextField()),
                ('Date_creation', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField()),
                ('commentaire', models.TextField(blank=True)),
                ('statut', models.CharField(choices=[('EN_COURS', 'En cours'), ('TERMINÉ', 'Terminé'), ('PAS_COMMENCÉ', 'Pas encore commencé')], default='PAS_COMMENCÉ', max_length=20)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
