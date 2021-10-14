from flask import Flask, request, Response, redirect
import json
import requests
from flask_cors import CORS

from flask.json import jsonify
from flask_pymongo import PyMongo
from bson import json_util

import views

app = Flask(__name__)
CORS(app)

mongo = PyMongo()
app.config["MONGO_URI"] = 'mongodb+srv://root:root@cluster0.nakfu.mongodb.net/ProblemFinder?retryWrites=true&w=majority'
mongo.init_app(app)


@app.route('/')
def index():
    return "Hello"


@app.route('/listar/websites', methods=['GET'])
def listawebsites():
    return views.listar_websites()


@app.route('/listar/setores/<int:id>', methods=['GET'])
def listasetores(id):
    url = views.url_website(id)

    listadesetores_antigo = views.listar_setores_antigo()
    listadesetores_web = views.listar_setores_web(1, url)
    listadesetores_novo = views.adicionar_novos_setores(listadesetores_antigo, listadesetores_web)

    json_data = json_util.dumps(listadesetores_web, ensure_ascii=False)
    print("=========listadesetores_web==========")
    print(json_data)
    return json_data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')