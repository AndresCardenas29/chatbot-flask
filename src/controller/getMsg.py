
import json
import random

from flask import jsonify
import json
import re


def response(data):
    iterData = json.loads(data)
    mensaje = iterData['mensaje']
    splitMensaje = re.split(r'\s|[,:;.?!-_!]\s*', mensaje.lower())
    response = checkAllMessages(splitMensaje)
    return response


def messageProbability(userMessage, recognizedWords, singleResponse=False, requiredWords=[]):
    messageCertainty = 0
    hasRequiredWords = True

    for word in userMessage:
        if word in recognizedWords:
            messageCertainty += 1

    porcentage = float(messageCertainty) / float(len(recognizedWords))

    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break
    if hasRequiredWords or singleResponse:
        return int(porcentage*100)
    else:
        return 0


def checkAllMessages(message):
    highestProb = {}

    def response(botResponse, listOfWords, singleResponse=False, requiredWords=[]):
        nonlocal highestProb
        highestProb[botResponse] = messageProbability(message, listOfWords, singleResponse, requiredWords)
        
    response(
      ['Hola!','Hola, como estas?','Hola buen dia!'][random.randrange(3)], 
      ['hola', 'muy buenas', 'buenas'], 
      singleResponse=True
    )
    response(
      'Estoy bien y tu?', 
      ['como', 'estas', 'vas', 'esta', 'va'], 
      requiredWords=['como']
    )
    response(
      'Estamos ubicados en x', 
      ['ubicados', 'direccion', 'donde', 'ubicacion'], 
      singleResponse=True
    )
    
    bestMatch = max(highestProb, key=highestProb.get)
    print(highestProb)

    return unknown() if highestProb[bestMatch] < 1 else bestMatch


def unknown():
    response = ['puedes decirlo de nuevo?',
                'No estoy seguro de lo que quieres'][random.randrange(2)]
    return response
