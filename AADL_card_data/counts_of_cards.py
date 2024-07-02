import pandas as pd

# this code counts up every duplicate item in the specified column, deletes the duplicates, and gives a number count in a new column

# read in the csv. the encoding here is just to make sure that python reads the CSV proeprly
df = pd.read_csv('path', encoding='latin1')

# counts the duplicates, deletes the duplicates, and adds a new column of counts
dupes = df.pivot_table(index = ['street1'], aggfunc ='size')

  
# keep the following line uncommented if you want to print the dataframe that was just created 
print(dupes)

# write dataframe to csv
dupes.to_csv('path')


print('Done')