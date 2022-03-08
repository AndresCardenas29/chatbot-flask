from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json

from src.controller.getMsg import response
from config import config

app = Flask(__name__, template_folder="src/view")
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/msg_bot', methods=['POST'])
def magBot():
    rspta = request.data
    rptaSend = response(rspta)
    # print("########################")
    # print(rptaSend)
    return jsonify(rptaSend)


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
