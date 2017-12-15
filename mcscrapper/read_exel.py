# Import pandas
import pandas as pd

filename = 'taglist.xlsx'

taglist = []

dframe = pd.read_excel(filename)
for i in dframe.index:
    data = {
        'name': dframe['name'][i],
        'url': dframe['url'][i]
    }
    taglist.append(data)
print(taglist)
    # print(dframe['name'][i])
    # print(dframe['url'][i])