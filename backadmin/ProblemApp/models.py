from django.db import models

class Setor(models.Model):
    SetorId = models.AutoField(primary_key=True)
    SetorNome = models.CharField(max_length=200)

class Website(models.Model):
    WebsiteId = models.AutoField(primary_key=True)
    WebsiteNome = models.CharField(max_length=200)
    WebsiteURL = models.CharField(max_length=500)
    WebsiteLogo = models.CharField(max_length=200)
    WebsiteCliques = models.PositiveIntegerField(default=0)

class Usuario(models.Model):
    UsuarioId = models.AutoField(primary_key=True)
    UsuarioNome = models.CharField(max_length=200)
    UsuarioSobrenome = models.CharField(max_length=200)
    UsuarioEmail = models.CharField(max_length=200)
    UsuarioSenha = models.CharField(max_length=200)
    UsuarioAlertas = models.BooleanField(default=False)
