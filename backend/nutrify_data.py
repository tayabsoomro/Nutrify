import requests
from bs4 import BeautifulSoup
import json


def CaloriKing():
	food_arr = raw_input("Enter the food name:")
	url = 'http://www.calorieking.com/foods/search.php?keywords='+food_arr+'&go=Search'
	response = requests.get(url).text
	soup = BeautifulSoup(response)
	main_wrapper = soup.find('div',attrs={'id':'search-results-content'})
	mini_wrappers = soup.findAll('div',attrs={'class':'food-search-result left-vertical-border-green'})
	first_url = mini_wrappers[0].findAll('a')
	for items in first_url:
		second_url = items['href']
		second_response = requests.get(second_url).text
		second_soup = BeautifulSoup(second_response)
		main_wrapper = second_soup.find('div',attrs={'class':'nutrient-facts'}).findAll('table')
		for attr_items in main_wrapper:
			dictionary = {}
			find_all_tds_value  = attr_items.findAll('td',attrs={'class':'label'})
			find_all_tds_amount = attr_items.findAll('td',attrs={'class':'amount'})
			for value_text, amount_text in zip(find_all_tds_value,find_all_tds_amount):
				dictionary[value_text.text] = amount_text.text
	with open(food_arr + '.json','wb') as outfile:
		json.dump(dictionary,outfile,indent=4)


def Clarifai():
	from clarifai.client import ClarifaiApi
	clarifai_api = ClarifaiApi()
	result = clarifai_api.tag_images(open('cucumber.jpg','rb'))
	response = result
	result_arr = response['results']
	for result_ind in result_arr:
		print result_ind['result']['tag']['classes']
Clarifai()