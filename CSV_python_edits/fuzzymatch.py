import pandas as pd
from fuzzywuzzy import process

# Still not sure about this one, from what I've seen so far, Fuzzy matching feels like a less reliable version of geocoding, but I'll leave this here for posterity

# read in csv's
df1 = pd.read_csv('C:/[path]/[csv name].csv', encoding='latin1') # the encoding here is just to make sure that python reads the CSV proeprly
df2 = pd.read_csv('C:/[path]/[csv name].csv', encoding='latin1')

# empty lists for storing the matches later 
match1 = []
match2 = []

list1 = df1['[name of column you want to match from CSV 1]'].tolist() 
list2 = df2['name of column you want to match from CSV 2'].tolist() 

threshold = 90 # this is the acceptable percentage threshold that the fuzzywuzzy plugin willtry to reach


# This for loop appends a new column for the matches it performs
for i in list1:
    match1.append(process.extract(i, list2, limit=2))
df1['matches'] = match1

print(df1)

df1.to_csv('C:/[path]/[name out outputted csv].csv')

print("Done")