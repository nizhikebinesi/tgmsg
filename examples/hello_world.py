from flask import Flask, request
from tgmsg import TelegramClient, messages

app = Flask(__name__)
client = TelegramClient('<YOUR_TOKEN>')


@client.register_message_processor()
def text_handler(incoming):
    msg = messages.TextMessage(incoming.message.text)
    client.send_message(msg, incoming.message.chat.id)


@app.route('/incoming')
def incoming():
    if request.json:
        client.process_json(request.json)
    return ''
