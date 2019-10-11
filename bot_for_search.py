import requests
import json
from requests_site import Main_words_for_search
import time

def items():
	k = requests.get('https://api.telegram.org/bot<token>/getUpdates')
	text_message = ((k.json())['result'][-1]['message']['text'])
	print(text_message)
	chat_id = ((k.json())['result'][-1]['message']['chat']['id'])
	return text_message, chat_id

if __name__ == '__main__':
	while True:
		text, chat_id = items()
		search = Main_words_for_search(text)
		search = search.data_send
		if search:
			for i in search:
				requests.get(('https://api.telegram.org/bot<token>/sendMessage?chat_id={0}&text={1}').format(chat_id, i))

		time.sleep(10)
