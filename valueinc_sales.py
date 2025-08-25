# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 22:09:16 2025

@author: Bulelani Thai
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')  <---format of read_csv

data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv', sep = ';')

#summary of the data
data.info()

#working with calculations

#Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased*SellingPricePerItem

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data ['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

#Sales Per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#Markup = (Sales - Cost)/Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#Rounding Marking

RoundMarkup = round(data['Markup'], 2)
data['Markup'] = round(data['Markup'], 2)

#Combining data fields

my_name = 'Dee'+'Naidoo'
my_date = 'Day'+'-'+'Month'+'-'+'Year'

#my_date = 'Day'+'-'

#checking columns data type
print(data['Day'].dtype)

#Change columns data type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)

my_date = day+'-'+data['Month']+'-'+year
data['Date'] = my_date

#using iloc to view specific columns/rows

data.iloc[0] #views the row with index = 0
data.iloc[0:3] #views the first 3 rows
data.iloc[-5:] #views the last 5 rows

data.head(5) #brings in the first 5 rows
data.iloc[:,2] #brings in all rows on the second column
data.iloc[4,2] #brings in fourth row, second column

#using split to split the client_keywords field
#new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

#creating new columns for the split columns in Client Keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']', '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep = ';')

#merging files: merge_df = pd.merge(old_df, new_df, on = 'key')
data = pd.merge(data, seasons, on = 'Month')

#dropping columns

#df = df.drop('ColumnName', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)

#to drop the columns simultaneously
data = data.drop(['Year', 'Month'], axis = 1)

#Export into CSV
data.to_csv('ValueInc_Cleaned.csv', index = False)










