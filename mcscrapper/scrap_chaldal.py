import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def chaldal_scrap():
	current_datetime = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
	filename = 'chaldal.xlsx'
	save_filename = "chaldal_updated_" + current_datetime + ".xlsx"
	writter = pd.ExcelWriter(path = save_filename, engine = 'openpyxl')

	dframe = pd.read_excel(filename, sheet_name=None)
	for sheet in dframe:
		product_data = []
		for i in dframe[sheet].index:
			discount_price = 0
			actual_price = 0
			url = dframe[sheet]['URL'][i]
			try:
				page = requests.get(url)
				soup = BeautifulSoup(page.content, 'html.parser')
				discount_price_col = soup.findAll('div', {'class':'discountedPriceSection'})
				for col in discount_price_col:
					discount_price = col.text.strip().split(' ')[0][1:-3]

				actual_price_col = soup.findAll('div', {'class':'fullPrice'})
				for col in actual_price_col:
					actual_price = col.text.strip().split(' ')[2]
				if actual_price == 0:
					actual_price_col = soup.findAll('div', {'class':'price'})
					for col in actual_price_col:
						actual_price = col.text.strip()[1:]
			except Exception as e:
				print(f"Error in url: {url}, error: {e}")
			data = {
				'URL': url,
				'Product_Name': dframe[sheet]['Product_Name'][i],
				'Quantity': dframe[sheet]['Quantity'][i],
				'Previous_Current_Price': dframe[sheet]['Current_Price'][i],
				'Previous_Actual_Price': dframe[sheet]['Actual_Price'][i],
				'Current_Price': discount_price,
				'Actual_Price': actual_price,
			}
			product_data.append(data)
		docData = pd.DataFrame( product_data )
		docData.to_excel(writter, sheet_name=sheet)
	writter.save()
	writter.close()


def chaldal_scrap_single_url():
	discount_price = 0
	actual_price = 0
	url = "https://chaldal.com/green-chilli-250-gm"
	try:
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		discount_price_col = soup.findAll('div', {'class':'discountedPriceSection'})
		for col in discount_price_col:
			discount_price = col.text.strip().split(' ')[0][1:-3]

		actual_price_col = soup.findAll('div', {'class':'fullPrice'})
		for col in actual_price_col:
			actual_price = col.text.strip().split(' ')[2]
		if actual_price == 0:
			actual_price_col = soup.findAll('div', {'class':'price'})
			for col in actual_price_col:
				actual_price = col.text.strip()[1:]
	except Exception as e:
		print(f"Error in url: {url}, error: {e}")
	print(actual_price, discount_price)
if __name__ == "__main__":
	chaldal_scrap()
	# chaldal_scrap_single_url()