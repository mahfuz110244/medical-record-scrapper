import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import time
import schedule

def func_scrap_chaldal():
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

def runs_my_script():
    func_scrap_chaldal()
    print(f"{datetime.now()} - Script executed successfully")

if __name__ == "__main__":
    print(f"start to run chaldal srcipt at {datetime.now()}")
    # schedule.every().hour.do(runs_my_script) # sets the function to run once per hour
    # schedule.every(10).seconds.do(runs_my_script) # sets the function to run per 10 second
    schedule.every(10).minutes.do(runs_my_script) # sets the function to run per 10 minutes  
    while True:  # loops and runs the scheduled job indefinitely 
        schedule.run_pending()
        time.sleep(1)