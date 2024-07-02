import pandas as pd
from fuzzywuzzy import process

# read in CSV's
df1 = pd.read_csv('path', encoding='latin1') # the encoding here is just to make sure that python reads the CSV proeprly
df2 = pd.read_csv('path', encoding='latin1') # df1 is the card data and df2 is the shapefile export

# empty lists for storing the matches later 
match1 = []
match2 = []

list1 = df1['street1'].tolist() 
list2 = df2['PROP_STREET'].tolist() 

threshold = 90 # this is the acceptable percentage threshold that the fuzzywuzzy plugin will try to reach


# This for loop appends a new column for the matches it performs
for i in list1:
    match1.append(process.extract(i, list2, limit=2))
df1['matches'] = match1

print(df1)

df1.to_csv('path') # write CSV to path

print("Done")