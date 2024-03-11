import pandas as pd

df = pd.read_csv("C:/[path]/[name of csv you want to use regex on].csv", encoding='latin1') # the encoding here is just to make sure that python reads the CSV proeprly

# this line of code removes periods in the specified column
df['street1'] = df['street1'].str.replace(r'\.', '', regex=True)



df.to_csv("C:/[path]/[name of outputted csv].csv", encoding='latin1')

print("Done")