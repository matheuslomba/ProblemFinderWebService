# Generated by Django 3.2.8 on 2021-10-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProblemApp', '0002_auto_20211011_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='UsuarioAlertas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='UsuarioEmail',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='UsuarioSenha',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='UsuarioSobrenome',
            field=models.CharField(default='teste', max_length=200),
        ),
    ]
