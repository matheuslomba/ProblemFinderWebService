# Generated by Django 3.2.8 on 2021-10-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProblemApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='UsuarioNome',
            field=models.CharField(default='teste', max_length=200),
        ),
        migrations.AlterField(
            model_name='setor',
            name='SetorNome',
            field=models.CharField(max_length=200),
        ),
    ]
