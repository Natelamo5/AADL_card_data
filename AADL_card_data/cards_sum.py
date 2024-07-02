import pandas as pd
import re

df = pd.read_csv('path', encoding='latin1')


# this code merges two specified CSV columns that contain integers
df['sum_of_cards'] = df.loc[:,['number_of_cards_x','number_of_cards_y']].sum(axis=1)

print(df)

df.to_csv('path')