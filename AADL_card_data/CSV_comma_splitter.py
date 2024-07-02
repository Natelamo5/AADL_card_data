import pandas as pd

df = pd.read_csv("path", encoding="latin1")

# this code splits one CSV entries on commas, was mostly used to clean up the geocoding results for joining with the shapefile

dfcleancsv = pd.concat([df['street_output'].str.split(', ', expand=True)], axis=1)

print(dfcleancsv)

dfcleancsv.to_csv("path", encoding="latin1")