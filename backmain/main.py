from os import name
from flask import Flask, request, Response, redirect
import json
import requests
#from flask_mongoalchemy import MongoAlchemy

from flask.json import jsonify
from flask_pymongo import PyMongo
from bson import json_util

import views

app = Flask(__name__)

mongo = PyMongo()
app.config["MONGO_URI"] = 'mongodb+srv://root:root@cluster0.nakfu.mongodb.net/ProblemFinder?retryWrites=true&w=majority'
mongo.init_app(app)

#Models
"""class Website(db.Model):
    WebsiteId = db.IntField(primary_key=True, autoincrement=False)
    WebsiteNome = db.StringField()
    WebsiteURL = db.StringField()
    WebsiteLogo = db.StringField()

class WebsiteUsuario(db.Model):
    WebsiteId = db.Column(db.Integer, primary_key=True)
    usuario_Id = db.IntField()
    website_Id = db.IntField()"""


@app.route('/')
def index():
    return "Hello"

@app.route('/listar/websites', methods=['GET'])
def listawebsites():
    return views.listar_websites()

"""@app.route('/clicar/websites/<int:id>', methods=['POST'])
def clicawebsites(id):
    return views.clicar_websites(request)"""

@app.route('/listar/setores/<int:id>', methods=['GET'])
def listasetores(id):
    url = views.url_website(id)

    listadesetores_antigo = views.listar_setores_antigo()
    listadesetores_web = views.listar_setores_web(1, url)#'https://g1.globo.com/')
    listadesetores_novo = views.adicionar_novos_setores(listadesetores_antigo, listadesetores_web)

    #print(Response(json.dumps(listadesetores_antigo), mimetype='application/json'))
    #print(Response(json.dumps(listadesetores_novo), mimetype='application/json'))
    
    """setores_collection = mongo.db.ProblemApp_setor
    setores_collection.insert_many([{'SetorNome' : "São Paulo"}, {'SetorNome' : "Rio de Janeiro"}], ordered=False)"""
    '''for setor in listadesetores_novo:
        print('--------------setor--------------')
        print(setor)
        res = requests.post('http://localhost:8080/setor', json={'SetorNome': setor})
        print('response from server', res.text)'''

    return "foi" #Response(json.dumps(listadesetores_novo), mimetype='application/json')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')