# Generated by Django 3.2.8 on 2021-10-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('SetorId', models.AutoField(primary_key=True, serialize=False)),
                ('SetorNome', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('UsuarioId', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('WebsiteId', models.AutoField(primary_key=True, serialize=False)),
                ('WebsiteNome', models.CharField(max_length=200)),
                ('WebsiteURL', models.CharField(max_length=500)),
                ('WebsiteLogo', models.CharField(max_length=200)),
                ('WebsiteCliques', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]