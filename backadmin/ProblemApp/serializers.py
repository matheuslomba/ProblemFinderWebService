from rest_framework import serializers
from ProblemApp.models import Setor, Website, Usuario

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ('SetorId', 'SetorNome')
    
class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('WebsiteId', 'WebsiteNome', 'WebsiteURL', 'WebsiteLogo', 'WebsiteCliques')
    
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('UsuarioId', 'UsuarioNome')
    
