# -*- encoding:utf-8 -*-
import transmissionrpc
import private
import telebot
import subprocess
import func
import json

subprocess.call(['transmission-daemon'])
bot = telebot.TeleBot(private.TOKEN)
tc = transmissionrpc.Client('localhost', port=9091)


def send(m, message_text):
    bot.send_message(m.chat.id, message_text)


try:
    subprocess.call(['mkdir', 'downloads'])
finally:
    pass

try:
    subprocess.call(['touch', 'pending.json'])
    with open('pending.json', 'w') as file:
        dct = {}
        json.dump(dct, file)
finally:
    pass


@bot.message_handler(commands='magnet')
def getmagnet(m):
    uid = m.from_user.id
    send(m, str(uid))
    text = m.text.split()
    if len(text) != 2:
        send(m, 'Usage: /magnet <url of magnet>')
    else:
        try:
            t = tc.add_torrent(text[1])
            send(m, 'Torrent added succesfully')
            with open('pending.json', 'r')as file:
                pending = json.load(file)
            if func.existeuser(uid, pending):
                pending[str(uid)].append(t.id)
            else:
                pending[str(uid)] = [t.id]
            with open('pending.json', 'w')as file:
                json.dump(pending, file)
        except:
            send(m, 'The link is not a valid magnet')


bot.polling()
