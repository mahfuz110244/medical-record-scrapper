from datetime import datetime
import pandas as pd

current_datetime = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
filename = 'chaldal.xlsx'
save_filename = "chaldal_" + current_datetime + ".xlsx"
writter = pd.ExcelWriter(path = save_filename, engine = 'openpyxl')

dframe = pd.read_excel(filename, sheet_name=None)
for sheet in dframe:
    product_data = []
    for i in dframe[sheet].index:
        data = {
            'Product_Name': dframe[sheet]['Product_Name'][i],
            'Quantity': dframe[sheet]['Quantity'][i],
            'Previous_Current_Price': dframe[sheet]['Current_Price'][i],
            'Previous_Actual_Price': dframe[sheet]['Actual_Price'][i],
            'URL': dframe[sheet]['URL'][i],
            'Current_Price': dframe[sheet]['Current_Price'][i],
            'Actual_Price': dframe[sheet]['Actual_Price'][i],
        }
        product_data.append(data)
    docData = pd.DataFrame( product_data )
    docData.to_excel(writter, sheet_name=sheet)
writter.save()
writter.close()