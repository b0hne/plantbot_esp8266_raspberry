"""
recieve data from esp and send telegram messages
"""
import socket
import telepot as pot
from telepot.loop import MessageLoop

s = socket.socket()
PORT = 1234
s.bind(('', PORT))
s.listen(3)

TELEBOT_ID = '<bot-token>'
CHAT_ID = '<your chat-id>'
"""
pybot for telegram control
"""

plants = {}
names = {'fpl':'linke Paprika im Fenster',
         'fpr':'rechte Paprika im Fenster',
         'fc':'Chilli im Fenster',
         'p':'Pomelo in der Küche',
         'cl':'linke Chilli in der Küche',
         'cr':'rechte Chilli in der Küche',
         'pl':'linke Paprika in der Küche',
         'pr':'rechte Paprika in der Küche'
        }

bot = pot.Bot(TELEBOT_ID)

def handle(msg):
    """
    any message requests plant status
    """
    print('handeling')
    chat_id = msg['chat']['id']
    print(plants)
    for item in plants:
        # print('item ', item)
        bot.sendMessage(chat_id, names[item] + ' ' + plants[item])


MessageLoop(bot, handle).run_as_thread()
"""
wait, store and send incoming data
"""
while True:
    plant = ''
    try:
        # print('try')
        c, addr = s.accept()
        plant = c.recv(1024).decode()
        c.close()
    except:
        # print('except')
        plant = '0'
    # print(plant)
    plant = plant.split()
    # print(plant[0])
    # print(plant[1])
    if plant != '0' and plant[0] in names:
        # print('if')
        plants[plant[0]] = plant[1]
        # print(plants)
    for item in plants:
        # print(item)
        if float(plants[item]) < 45:
            if item not in names:
                # print('item not in names')
                bot.sendMessage(CHAT_ID, 'new entry: ' + item + ' : ' + plants[item])
            else:
                # print('item in names')
                bot.sendMessage(CHAT_ID, names[item] + ' ' + plants[item])
