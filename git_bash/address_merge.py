import pandas as pd
import re

# this code merges two CSVs (in this case, the card data and shapefile export) without omitting the non-matches

df1 = pd.read_csv('C:/[path]/[csv card data here].csv', encoding='latin1') # the encoding here is just to make sure that python reads the CSV proeprly

df2 = pd.read_csv('C:/[path]/[exported shapefile as csv here].csv', encoding='latin1')

merged_df = df1.merge(df2, left_on='[name of streets column in shapefile csv]', right_on='[name of streets column in card data csv]', how='right')

merged_df.to_csv('C:/[path]/[name of new csv created from merge].csv') # writing new csv from merge

print('Done')

