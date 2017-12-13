#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
data_tag = {
    'name' : [],
	'url' : []
	}
base = "https://www.medicinenet.com"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for letter in alphabet:
	page = requests.get("https://www.medicinenet.com/diseases_and_conditions/alpha_" + letter + ".htm")
	soup = BeautifulSoup(page.content, 'html.parser')
	# [s.extract() for s in soup([ 'script', '[document]', 'head', 'title'])]
	all_col = soup.findAll(id="AZ_container")
	for col in all_col:
		list_data = col.find_all('li')
		for ld in list_data:
			# print(ld)
			data_tag['name'].append(ld.find("a").getText().strip())
			data_tag['url'].append(urljoin(base, ld.find("a").get('href')))
			# print(urljoin(base, ld.find("a").get('href')))
			# print(ld.find("a").getText().strip())
	# print(data)
docData = pd.DataFrame( data_tag )
docData.to_excel("taglist.xlsx")

data_vital = {
    'name' : [],
	'url' : []
	}
# for Procedure & Test A-Z List
for letter in alphabet:
	page = requests.get("https://www.medicinenet.com/procedures_and_tests/alpha_" + letter + ".htm")
	soup = BeautifulSoup(page.content, 'html.parser')
	# [s.extract() for s in soup([ 'script', '[document]', 'head', 'title'])]
	all_col = soup.findAll(id="AZ_container")
	for col in all_col:
		list_data = col.find_all('li')
		for ld in list_data:
			# print(ld)
			data_vital['name'].append(ld.find("a").getText().strip())
			data_vital['url'].append(urljoin(base, ld.find("a").get('href')))
			# print(urljoin(base, ld.find("a").get('href')))
			# print(ld.find("a").getText().strip())
	# print(data)
docData = pd.DataFrame( data_vital )
docData.to_excel("vitallist.xlsx")
