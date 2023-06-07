from datetime import datetime
import time
import requests
from flask import Flask, render_template, request, redirect, json
from firebase import firebase
import json

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://sd-cesar-7789b-default-rtdb.firebaseio.com/', None)
link = "https://sd-cesar-7789b-default-rtdb.firebaseio.com/"


@app.route('/')
def red():
    return redirect('/welcome')


@app.route('/welcome')
def welcome():
    return render_template('index.html')


@app.route('/plantinhas', methods=['GET', 'POST'])
def plants():
    # Dando get no nome das plantas
    plants = []
    requisition = requests.get(f'{link}/plantas/.json')
    dic = requisition.json()
    for i in dic:
        plants.append(i)
    # Tentando botar pop-up javaScript na tela, caso planta já esteja cadastrada
    nome_ja_registrado = 0
    # Método post pra adicionar nova planta
    if request.method == 'POST':
        hoje_dia = time.strftime("%d-%m-%Y") # Pegar hora adicionada
        agora = datetime.now() # Pegar hora adicionada
        hora = agora.strftime("%H:%M:%S") # Pegar hora adicionada
        infos_tempo = hoje_dia + ' ' + hora # Pegar hora adicionada

        nome_nova_planta = request.form['nome_planta'].capitalize() # Pegando nome do html

        if nome_nova_planta not in dic: # Conferindo se planta não já está no banco pelo nome dela
            infos_tempo_inserir = {'data': infos_tempo} # Dicionario com hora no value e data na key, para dar o post
            requests.patch(f'{link}/plantas/{nome_nova_planta}/.json', data=json.dumps(infos_tempo_inserir))#Post(patch)
            return redirect('/plantinhas') # Quando inserida planta atualizar a pagina automaticamente
        else: # Else, nao precisa de explicaçao
            print("nome já registrado")
            nome_ja_registrado = 1
    return render_template('plantas.html', nome_ja_registrado=nome_ja_registrado, dic=dic)


if __name__ == '__main__':
    app.run(debug=False)
