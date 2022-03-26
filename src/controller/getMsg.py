
import json
import re
import random

from flask import jsonify

# funcion para enviar y recibir mensajes
def response(data): # recibe un mensaje de tipo json
    iterData = json.loads(data) # pasa el json a dato python
    mensaje = iterData['mensaje'] # se obtiene el mensaje del json
    splitMensaje = re.split(r'\s|[,:;.?!-_!]\s*', mensaje.lower()) # se remueve los caracteres especiales, simbolos y signos
    response = checkAllMessages(splitMensaje) # envia el mensaje y retorna un mensaje del bot
    return response # se retorna el mensaje

# funcion para obtener la probabilidad
def messageProbability(userMessage, recognizedWords, singleResponse=False, requiredWords=[]):
    # obtiene el mensaje de usuario, palabras reconocidas, respuesta unitaria y palabras requeridas
    
    # certeza del mensaje
    messageCertainty = 0
    # si requeire o no palabras
    hasRequiredWords = True
    
    # recorre el mensaje del usuario
    for word in userMessage:
        # si la palabra del mensaje es reconozida, la certeza aumenta de 1
        if word in recognizedWords:
            messageCertainty += 1

    # se multiplica la certeza por 100 y para calcular un porcentaje
    porcentage = float(messageCertainty) / float(len(recognizedWords))

    # recorre el mensaje del usuario
    for word in requiredWords:
        # si no encuentra una palabra requerida
        if word not in userMessage:
            # palabras requerias es falso
            hasRequiredWords = False
            break
        
    # si tiene palabras requeridas o palabras simples
    if hasRequiredWords or singleResponse:
        # retorna el porcentaje por 100
        return int(porcentage*100)
    else:
        # sino, es porque no se encontro ninguna palabra que tenga algun parentesco
        return 0

# Verifica todos los mensajes
def checkAllMessages(message):
    highestProb = {} # diccionario con la probabilidad mas alta

    # recorre todos los mensajes
    def response(botResponse, listOfWords, singleResponse=False, requiredWords=[]):
        nonlocal highestProb # se usa la variable global
        # obtiene la probabilidad del mensaje
        highestProb[botResponse] = messageProbability(
            message, listOfWords, singleResponse, requiredWords)

    # mensajes de bienvenida
    response(
        ['Hola!', 'Hola, como estas?', 'Hola buen dia!'][random.randrange(3)],
        ['hola', 'muy buenas', 'buenas'],
        singleResponse=True
    )

    # mensajes de respuesta
    response(
        'Estoy bien y tu?',
        ['como', 'estas', 'vas', 'esta', 'va'],
        requiredWords=['como']
    )
    # mensajes de despedida
    response(
        'Estamos ubicados en x',
        ['ubicados', 'direccion', 'donde', 'ubicacion'],
        singleResponse=True
    )

    # retorna el mensaje mas probable
    bestMatch = max(highestProb, key=highestProb.get)
    print(highestProb) # imprime la probabilidad

    
    return unknown() if highestProb[bestMatch] < 1 else bestMatch

# Respuesta desconocida
def unknown():
    response = ['puedes decirlo de nuevo?',
                'No estoy seguro de lo que quieres'][random.randrange(2)]
    return response
