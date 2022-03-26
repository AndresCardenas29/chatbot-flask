from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
import json

from src.controller.getMsg import response
from config import config

# en template_folder se da la ruta para las vistas html
app = Flask(__name__, template_folder="src/view") 
CORS(app) # CORS

# ruta para generar una vista y hacer uso del bot
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # muestra el archivo index.html

# ruta post que recibe el mensaje del usuario para
# y responde un mensaje generado por el bot
@app.route('/msg_bot', methods=['POST'])
def magBot():
    rspta = request.data # obtiene el mensaje del usuario
    rptaSend = response(rspta) # envia el mensaje al bot, y recibe una respuesta
    return jsonify(rptaSend) # envia la respuesta como JSON

# retorna una url incorrecta a home del bot
@app.route('/*', methods=['GET'])
def default():
    return redirect('/')


if __name__ == '__main__':
    app.config['DEBUG'] = True # Activar el modo desarrollador
    app.run(host="0.0.0.0",port=3000) # host y puertos
