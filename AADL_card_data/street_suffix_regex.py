import pandas as pd
import re

df = pd.read_csv("path", encoding='latin1') # reads in the CSV. The encoding is just to make sure that python reads the CSV proeprly
print(df.head())


# these lines of code removes unnecessary periods in the specified column
df['street1'] = df['street1'].str.replace(r'\.', '', regex=True)
df['street1'] = df['street1'].str.replace(r'\,', '', regex=True)


# these lines replace street suffixes with shorthand to match the shapefile
df['street1'] = df['street1'].str.replace(r' STREET.*', ' ST', regex=True)
df['street1'] = df['street1'].str.replace(r' AVENUE.*', ' AV', regex=True)
df['street1'] = df['street1'].str.replace(r' AVE.*', ' AV', regex=True)
df['street1'] = df['street1'].str.replace(r' CIRCLE.*', ' CIR', regex=True)
df['street1'] = df['street1'].str.replace(r' COURT.*', ' CT', regex=True)
df['street1'] = df['street1'].str.replace(r' DRIVE.*', ' DR', regex=True)
df['street1'] = df['street1'].str.replace(r' LANE.*', ' LN', regex=True)
df['street1'] = df['street1'].str.replace(r' BOULEVARD.*', ' BLV', regex=True)
df['street1'] = df['street1'].str.replace(r' BLVD.*', ' BLV', regex=True)
df['street1'] = df['street1'].str.replace(r' ROAD.*', ' RD', regex=True)
df['street1'] = df['street1'].str.replace(r' PLACE.*', ' PL', regex=True)
df['street1'] = df['street1'].str.replace(r'ANN ARBOR - SALINE', 'ANN ARBOR-SALINE', regex=True)
df['street1'] = df['street1'].str.replace(r'  ', ' ', regex=True)
df['street1'] = df['street1'].str.replace(r'^ +| +$', '', regex=True)


# removes everything including and following a '#', mostly for street addresses and not apartments
df['street1'] = df['street1'].str.replace(r'#.*', '', regex=True)


# removes everything including and following "APT", same as the above line
df['street1'] = df['street1'].str.replace(r'APT.*', '', regex=True)


# removes everything including and following "SUITE", same as above
df['street1'] = df['street1'].str.replace(r'SUITE.*', '', regex=True)


# these lines are the same as the street suffix regex above, but for the few street addresses in street2
# df['street2'] = df['street2'].str.replace(r' STREET.*', ' ST', regex=True)
# df['street2'] = df['street2'].str.replace(r' AVENUE.*', ' AV', regex=True)
# df['street2'] = df['street2'].str.replace(r' AVE.*', ' AV', regex=True)
# df['street2'] = df['street2'].str.replace(r' CIRCLE.*', ' CIR', regex=True)
# df['street2'] = df['street2'].str.replace(r' COURT.*', ' CT', regex=True)
# df['street2'] = df['street2'].str.replace(r' DRIVE.*', ' DR', regex=True)
# df['street2'] = df['street2'].str.replace(r' LANE.*', ' LN', regex=True)
# df['street2'] = df['street2'].str.replace(r' BOULEVARD.*', ' BLV', regex=True)
# df['street2'] = df['street2'].str.replace(r' BLVD.*', ' BLV', regex=True)
# df['street2'] = df['street2'].str.replace(r' ROAD.*', ' RD', regex=True)
# df['street2'] = df['street2'].str.replace(r' PLACE.*', ' PL', regex=True)


# writes regex'ed code to new file
df.to_csv("path", encoding='latin1')

