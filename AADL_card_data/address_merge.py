import pandas as pd
import re

# this code merges two CSVs (in this case, the card data and shapefile export) without omitting the non-matches

df1 = pd.read_csv('path', encoding='latin1') # this is the shapefile export

df2 = pd.read_csv('path', encoding='latin1') # this is the card data

merged_df = df1.merge(df2, left_on='street1', right_on='street1', how='outer')

num_of_rows = len(merged_df)

print(f"The number of rows is {num_of_rows}")

merged_df.to_csv('path') # writing new csv from merge

print('Done')