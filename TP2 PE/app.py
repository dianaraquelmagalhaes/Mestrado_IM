from flask import Flask, render_template, request, redirect
import requests
import json

import db_relatorios
from povoamento import relatorios

app = Flask(__name__)

for relatorio in relatorios:
    db_relatorios.insert(relatorio)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/relatorios', methods=['GET'])
def get_relatorios():
    res = requests.get('http://localhost:5000/api/relatorios')
    ps = json.loads(res.content)
    return render_template('relatorios_view.html', title='Relatórios', relatorios=ps)


@app.route('/relatorios', methods=['POST'])
def post_relatorio():
    data = dict(request.form)
    requests.post('http://localhost:5000/api/relatorios', data=data)
    return redirect('http://localhost:5000/relatorios')

@app.route('/relatorios/<titulo>', methods=['GET'])
def get_relatorio(titulo):
    res = requests.get('http://localhost:5000/api/relatorios/' + titulo)
    p = json.loads(res.content)
    return render_template('relatorio_view.html', p=p)


# API
@app.route('/api/relatorios', methods=['GET'])
def api_get_relatorios():
    ps = db_relatorios.find_all()
    return json.dumps(ps)


@app.route('/api/relatorios', methods=['POST'])
def api_post_relatorio():
    data = dict(request.form)
    print(data)
    db_relatorios.insert(data)

    return json.dumps(db_relatorios.find_all())

@app.route('/api/relatorios/<titulo>', methods=['GET'])
def api_get_relatorio(titulo):
    p = db_relatorios.find_one(titulo)
    return json.dumps(p)

@app.route('/relatorios/<titulo>/remove', methods=['POST'])
def remove_relatorio(titulo):
    requests.post('http://localhost:5000/api/relatorios/' + titulo+"/remove")
    return redirect('http://localhost:5000/relatorios')

@app.route('/api/relatorios/<titulo>/remove', methods=['POST'])
def api_remove_relatorio(titulo):
    p= db_relatorios.remove(titulo)
    print("apaguei")
    res = requests.get('http://localhost:5000/api/relatorios/')
    print(res)
    return json.dumps(p)


@app.route('/relatorios/<titulo>/alterar', methods=['POST'])
def alterar_relatorio(titulo):
    requests.post('http://localhost:5000/api/relatorios' + titulo + "/alterar")
    res = requests.get('http://localhost:5000/api/relatorios/' + titulo)
    p = json.loads(res.content)
    return render_template('alterar_view.html', p=p)


@app.route('/api/relatorios/<titulo>/alterar', methods=['POST'])
def api_alterar_relatorio(titulo):
    p= db_relatorios.remove(titulo)
    data = dict(request.form)
    print(data)
    db_relatorios.insert(data)
    res = requests.get('http://localhost:5000/api/relatorios/')
    return redirect('http://localhost:5000/relatorios')
    


# Pessoas
@app.route('/pessoas', methods=['GET'])
def get_pessoas():

    res = requests.get('http://localhost:5000/api/pessoas')
    ps = json.loads(res.content)
    return render_template('pessoas_view.html', title='Pessoas', pessoas=ps)


@app.route('/pessoas/<numero>', methods=['GET'])
def get_pessoa(numero):

    res = requests.get('http://localhost:5000/api/pessoas/%s' % numero)
    p = json.loads(res.content)
    return render_template('pessoa_view.html', pessoa=p)



import db_pessoas

# API
@app.route('/api/pessoas', methods=['GET'])
def api_get_pessoas():

    ps = db_pessoas.find_all()

    return json.dumps(ps)



@app.route('/api/pessoas/<numero>', methods=['GET'])
def api_get_pessoa(numero):

    d = pessoas[numero]
    d['numero'] = numero
    
    return json.dumps(d)


@app.route('/api/pessoas', methods=['POST'])
def api_post_pessoa():

    data = dict(request.form)
    db_pessoas.insert(data)

    return data

#ALTERAR

    

