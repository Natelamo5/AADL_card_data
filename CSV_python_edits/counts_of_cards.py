import pandas as pd

# this code counts up every duplicate item in the specified column, deletes the duplicates, and gives a number count in a new column

# read in the csv
df = pd.read_csv('C:/[path]/[csv you want to count duplicate rows in].csv', encoding='latin1') # the encoding here is just to make sure that python reads the CSV proeprly

# counts the duplicates, deletes the duplicates, and adds a new column of counts
dupes = df.pivot_table(index = ['[name of column you want to count duplicates in]'], aggfunc ='size')
  
# keep this uncommented if you want to print the dataframe that was just created 
print(dupes)

# print dataframe to csv
dupes.to_csv('C:/[path]/[name out outputted csv].csv')


print('Done')