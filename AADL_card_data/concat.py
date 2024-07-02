import pandas as pd 
  
# # concat two csv files 

df = pd.concat( 
    map(pd.read_csv, ['path', 'path']), ignore_index=True) 
print(df) 

df.to_csv('path')