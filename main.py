import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


updater = Updater(token='5711589626:AAEGLRamCRUYuAoVF4XR0g4qNL8c7tHsA3g', use_context=True)
#Dispatcher para crear los comandos
dispatcher = updater.dispatcher

#Funcion que consulta a la api el valor del DolarBlue
def dolarBlue(update, context):
    response = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
    if (response.status_code==200):
        data = response.json()
        fecha = data['fecha']
        precio_compra = data['compra']
        precio_venta = data['venta']

        message = f"""Para la fecha {fecha}
        el precio de la compra es {precio_compra}
        el precio de la venta es {precio_venta}"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else: 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, algo salio mal")

def dolarTurista(update, context):
    response = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarturista')
    if (response.status_code==200):
        data = response.json()
        context.bot.send_message(chat_id=update.effective_chat.id, text=data)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, algo salio mal")


#Funcion que contesta a comandos desconocidos
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="No reconozco ese comando")

#Linkeo los comandos a las funciones y agrego los handlers

#Dolar Blue
dolarblue_handler = CommandHandler('dolarblue', dolarBlue)
dispatcher.add_handler(dolarblue_handler)

#Dolar Turista
dolarTurista_handler = CommandHandler('dolarturista', dolarTurista)
dispatcher.add_handler(dolarTurista_handler)

#Comando desconocido
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
