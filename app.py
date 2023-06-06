from datetime import datetime
import time
import requests
from flask import Flask, render_template, request, redirect, json
from firebase import firebase
import json

app = Flask(__name__)
firebase = firebase.FirebaseApplication('https://sd-cesar-7789b-default-rtdb.firebaseio.com/', None)
link = "https://sd-cesar-7789b-default-rtdb.firebaseio.com/"
hoje_dia = time.strftime("%d-%m-%Y")
agora = datetime.now()
hora = agora.strftime("%H:%M:%S")
infos_tempo = hoje_dia + ' ' + hora


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/plantinhas', methods=['GET', 'POST'])
def plants():
    if request.method == 'POST':
        nome_nova_planta = request.form['nome_planta']
        requisicao_planta_nova = requests.post(f'{link}/plantas/{nome_nova_planta}.json', data=json.dumps('hash ind.'))

        print(requisicao_planta_nova)
    else:
        return render_template('plantas.html')

    return render_template('plantas.html')


if __name__ == '__main__':
    app.run(debug=True)
