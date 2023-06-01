from datetime import datetime
import time
import requests
from flask import Flask, render_template, request, redirect, json
from firebase import firebase
import json

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://sd-cesar-7789b-default-rtdb.firebaseio.com/', None)
link = "https://sd-cesar-7789b-default-rtdb.firebaseio.com/plantas"
hoje_dia = time.strftime("%d-%m-%Y")
agora = datetime.now()
hora = agora.strftime("%H:%M:%S")


#def get_plantas(rota_banco_individual):
headings = []
plants_info = []
requisicao = requests.get(f'{link}/.json')
dic_requisicao = requisicao.json()
informacoes_plantas_individual = dic_requisicao

for id_dono_planta in dic_requisicao:
    nome_planta = dic_requisicao[id_dono_planta]['nome']
    headings.append(nome_planta)
    plants_info.append(dic_requisicao[id_dono_planta])
    print(f'nome planta: {nome_planta}, id individual planta: {id_dono_planta}')
    print(f'todas as infos: {informacoes_plantas_individual}\n')

print('print individual das listas:\n', headings, '\n', plants_info)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/plantas')
def plantas():
    return render_template('plantas.html')


if __name__ == '__main__':
    app.run()
