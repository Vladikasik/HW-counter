import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClothesShop.settings")
django.setup()

import telebot
import config

import messages as ms

class Bot:

    def __init__(self):

        self.bot = telebot.TeleBot(config.token)
    
    def mainloop(self):

        @self.bot.message_handler(commands=['start', 'help', 'add_task', 'profile'])
        def commands(msg):

            if msg.text == '/start':
                self.bot.send_message(msg.chat.id, ms.start)
            elif msg.text == '/help':
                self.bot.send_message(msg.chat.id, ms.commands)
            elif msg.text == '/add_task':
                pass
            elif msg.text == '/profile':
                pass
            else:
                pass
        
        self.bot.polling()
    
if __name__ == '__main__':
    bot = Bot()
    print(f'Bot initialized with token ')
    bot.mainloop()