# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import re

import collections.abc
collections.Hashable = collections.abc.Hashable
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crear una instancia de ChatBot
bot = ChatBot(
    'chatbot',
    read_only=False,
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Lo siento, no entiendo esa pregunta.😔',
            'maximum_similarity_threshold': 0.95,
        }
    ]
)

# Lista de preguntas y respuestas con información sobre ti
list_to_train = [
# Preguntas y respuestas aquí ...
    "Hola",
    "¡Hola! ¿Cómo estás?",
    "quien es tu creador",
    "El grupo 1 inmobiAI",
    "¿Cuál es tu comida favorita?",
    "Me gusta el helado",
    "¿Cuál es tu deporte favorito?",
    "Me gusta el fútbol",
    "¿Tienes hijos?",
    "No, soy un programa de computadora",
    "¿Cual es tu nombre?",
    "Mi nombre es InmobiAI",
    "¿Que vendes?",
    "Casas",
    "¿Cuánto esta una casa?",
    "podrias predecirlo tu segun tus gustos",
    "¿Qué te gusta hacer en tu tiempo libre?",
    "Me gusta aprender nuevas cosas",
    "¿Cuál es tu color favorito?",
    "Me encanta el azul",
    "¿Me ayudarias?",
    "por su puesto, tiene que ir a la seccion cotizaciones",
    "¿Cuál es tu pasatiempo favorito?",
    "Disfruto leyendo y escribiendo",
    "Gracias",
    "A ti, vuelve cuando quieras",
    "¿Tienes hermanos o hermanas?",
    "Soy un programa informático, así que no tengo familia",
    "¿Dónde vives?",
    "Soy un bot virtual, no tengo una ubicación física",
    "¿Cuál es tu deporte favorito?",
    "Me gusta el tenis",

]
# Limpiar los caracteres de puntuación de la lista de entrenamiento
def clean_text(text):
    return re.sub(r'[.,!?]', '', text)

list_to_train = [clean_text(text) for text in list_to_train]

# Entrenar el bot con el entrenador ChatterBotCorpusTrainer
trainer = ChatterBotCorpusTrainer(bot)

# Entrenar el bot con el corpus de entrenamiento en inglés
trainer.train('chatterbot.corpus.spanish')

# Ahora el bot está listo para responder a las preguntas

# Entrenar el bot con la lista personalizada de preguntas y respuestas #se puede quitar
#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)



def chatbots(request):
    return render(request, 'index2.html')



def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)