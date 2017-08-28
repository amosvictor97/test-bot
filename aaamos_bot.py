import requests
from time import sleep
import datetime


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
            method = 'getUpdates'
            params = {'timeout': timeout, 'offset': offset}
            resp = requests.get(self.api_url + method, params)
            result_json = resp.json()['result']  # renvoi une liste
            print(result_json)
            for elt in result_json:
                print(elt)
            return result_json

    def send_message(self, chat_id, text):
            params = {'chat_id': chat_id, 'text': text}
            method = 'sendMessage'
            resp = requests.post(self.api_url + method, params)
            return resp

    def get_last_update(self):
            get_result = self.get_updates()
            if len(get_result) > 0:
                last_update = get_result[-1]
            else:
                print("longueur du result")
                print(len(get_result))
                total_update = len(get_result)
                print(total_update)
                last_update = get_result[total_update]
            return last_update

    def get_update_id(self):
        id = self.get_updates()[-1]['update_id']
        return id

    def get_chat_text(self):
        chat_text = self.get_updates()[-1]['message']['text']
        return chat_text

    def get_chat_id(self):
        chat_id = self.get_updates()[-1]['message']['chat']['id']
        return chat_id

    def get_chat_name(self):
        chat_name = self.get_updates()[-1]['message']['chat']['first_name']
        return chat_name
# fin definition de la classe


# utilisation
token = "417944781:AAFV_u2ZZ--29rfeYh33kF2-Z9-nj4dv36Y"
greet_bot = BotHandler(token)
greetings = ('hello', 'hi', 'greetings', 'sup')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour
    while True:
        print('execution loop')
        updateId = greet_bot.get_update_id()
        print('valeur du update id')
        print(updateId)
        last_update_id = updateId
        last_chat_text = greet_bot.get_chat_text
        last_chat_id = greet_bot.get_chat_id
        last_chat_name = greet_bot.get_chat_name

        # greet_bot.get_updates(new_offset)
        # last_update = greet_bot.get_last_update()
        #  last_update_id = last_update['update_id']
        # last_update_id = updateId[-1]['update_id']
        # last_chat_text = last_update['message']['text']
        # last_chat_id = last_update['message']['chat']['id']
        # last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Morning  {}'
                                   .format(last_chat_name))
            today += 1
        elif last_chat_text in greetings and today == now.day and 12 <= hour < 17:
                    greet_bot.send_message(last_chat_id, 'Good Afternoon {}'
                                           .format(last_chat_name))
                    today += 1
        elif last_chat_text in greetings and today == now.day and 17 <= hour < 23:
                    greet_bot.send_message(last_chat_id, 'Good Evening  {}'
                                           .format(last_chat_name))
                    today += 1
        new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
