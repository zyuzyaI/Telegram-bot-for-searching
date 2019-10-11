"""Search on www.olx.ua products for search terms and return
a list of 5 new products that do not see the previous search."""

import requests
from bs4 import BeautifulSoup
import shelve


class Main_words_for_search:
	def __init__(self, message):
		self.message = message
		self.search_url = self.search_word(self.message)
		self.file_dict = self.data_item(self.search_url)
		self.data_send = self.shelve_file(self.file_dict)

	def shelve_file(self, file_dict):
		# create database key -> value
		try:
			our_data = shelve.open('our_data_base') # create db file
			lst_send = []
			# cycle 'for' checking old db-file if we get a new item then they will be added to list_send
			for i in file_dict:
				if i not in our_data:
					lst_send.append(file_dict[i])
			our_data.clear()
			# upgrade db
			for i in file_dict:
				our_data[i] = file_dict[i]
			our_data.close()
			return lst_send   # return list of new item
		# block  'except' create new db and delet old file
		except:
			our_data = shelve.open('our_data_base', 'n')
			our_data.close()
			return [] 	# if error return emty list


	def search_word(self, message):
		# create our url for search
		search_input_tmp = message.split()
		search_input = '-'.join(search_input_tmp)
		url_olx = 'https://www.olx.ua/uk/list/q-{}/'.format(search_input)
		return url_olx

	def get_html(self, url):
		# get html text
		return requests.get(url)

	def data_item(self, url):
		html = self.get_html(url)
		soup = BeautifulSoup(html.text, 'lxml')
		pat_item = soup.find('table', class_='fixed offers breakword redesigned').find_all('div', class_='offer-wrapper')
		dict_tmp = {}
		for i in range(5):
			tmp = pat_item[i].find('h3', class_='lheight22 margintop5')
			name = tmp.text.strip()
			url = tmp.find('a')['href']
			dict_tmp[name] = url
		return dict_tmp
