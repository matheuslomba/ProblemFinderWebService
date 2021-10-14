from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

import random

from .models import Setor, Website, Usuario
from .serializers import SetorSerializer, WebsiteSerializer, UsuarioSerializer
from .producer import publish

#Guardar imagens
from django.core.files.storage import default_storage

@csrf_exempt
def setorApi(request, id=0):    
    if request.method == 'GET':
        setores = Setor.objects.all()
        setores_serializer = SetorSerializer(setores, many=True)
        return JsonResponse(setores_serializer.data, safe=False)

    elif request.method == 'POST':
        setor_data = JSONParser().parse(request)
        setores_serializer = SetorSerializer(data = setor_data)
        if setores_serializer.is_valid():
            setores_serializer.save()
            #publish("Adicionado com sucesso", setores_serializer.data)
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)

    elif request.method == 'PUT':
        setor_data = JSONParser().parse(request)
        setor = Setor.objects.get(SetorId=setor_data['SetorId'])
        setores_serializer = SetorSerializer(setor, data = setor_data)
        if setores_serializer.is_valid():
            setores_serializer.save()
            #publish("Atualizado com sucesso", setores_serializer.data)
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar")
    
    elif request.method == 'DELETE':
        setor = Setor.objects.get(SetorId = id)
        setor.delete()
        #publish("Deletado com sucesso", id)
        return JsonResponse("Deletado com sucesso", safe=False)

@csrf_exempt
def websiteApi(request, id=0):    
    if request.method == 'GET':
        websites = Website.objects.all()
        websites_serializer = WebsiteSerializer(websites, many=True)
        return JsonResponse(websites_serializer.data, safe=False)

    elif request.method == 'POST':
        website_data = JSONParser().parse(request)
        websites_serializer = WebsiteSerializer(data = website_data)
        if websites_serializer.is_valid():
            websites_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)

    elif request.method == 'PUT':
        website_data = JSONParser().parse(request)
        website = Website.objects.get(WebsiteId=website_data['WebsiteId'])
        websites_serializer = WebsiteSerializer(website, data = website_data)
        if websites_serializer.is_valid():
            websites_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar")
    
    elif request.method == 'DELETE':
        website = Website.objects.get(WebsiteId = id)
        website.delete()
        return JsonResponse("Deletado com sucesso", safe=False)

@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        print("--------usuarios-------")
        print(usuarios)
        usuario = random.choice(usuarios)
        print("--------usuario-------")
        print(usuario)
        usuario_serializer = UsuarioSerializer(usuario, many=False)
        print("--------usuario serializer-------")
        print(usuario_serializer)
        return JsonResponse(usuario_serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        print("----------------usuario_data---------------")
        print(usuario_data)
        usuarios_serializer = UsuarioSerializer(data = usuario_data)
        print("----------------usuarios_serializer-----------------")
        print(usuarios_serializer)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)

    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuario.objects.get(UsuarioId=usuario_data['UsuarioId'])
        usuarios_serializer = UsuarioSerializer(usuario, data = usuario_data)
        if usuarios_serializer.is_valid():
            usuarios_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar")
    
    elif request.method == 'DELETE':
        usuario = Usuario.objects.get(UsuarioId = id)
        usuario.delete()
        return JsonResponse("Deletado com sucesso", safe=False)


@csrf_exempt
def SalvarArquivo(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)