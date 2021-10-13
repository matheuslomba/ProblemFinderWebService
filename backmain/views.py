from flask import Flask, request, Response
from flask.json import jsonify
from bson import json_util
from main import mongo
#from main import db

from procuraWeb import mainbusca
"""import os, sys
scriptWebPath = os.path.abspath('../ScriptWeb')
sys.path.insert(0, scriptWebPath)
from procuraWeb import mainbusca"""

def listar_setores_antigo():
    setores_collection = mongo.db.ProblemApp_setor
    setores = setores_collection.find()
    lista_setores = list(setores)
    lista_setores_ok = []
    for d in lista_setores:
        if d['SetorNome'] not in lista_setores_ok:
            lista_setores_ok.append(d['SetorNome'])
    print(lista_setores_ok)
    return lista_setores_ok

def listar_setores_web(metodo, url):
    setores = mainbusca(metodo, url)
    print('---------setores---------')
    print(setores)
    return setores

def adicionar_novos_setores(listadesetores_antigo, listadesetores_web):
    listadesetores_novo = []
    for s in listadesetores_web:
        if s not in listadesetores_antigo:
            listadesetores_novo.append(s)

    print(listadesetores_novo)
    #setores_collection = mongo.db.ProblemApp_setor
    #for setor in listadesetores_novo:
    #setores_collection.insert_one({'SetorNome' : "São Paulo"})
    
    return listadesetores_novo


def listar_websites():
    website_collection = mongo.db.ProblemApp_website
    websites = website_collection.find()
    lista_websites = list(websites)
    json_data = json_util.dumps(lista_websites)
    return json_data

def clicar_websites(request):
    website_collection = mongo.db.ProblemApp_website
    website = request.json['cliques']
    print("-----------website---------")
    print(website)
    return 'foi'

def url_website(id):
    website_collection = mongo.db.ProblemApp_website
    website = website_collection.find_one( {"WebsiteId": id} )
    url = website['WebsiteURL']
    return url