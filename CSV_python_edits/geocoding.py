import pandas as pd
import geopandas
import geopy
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim



df = pd.read_csv('C:/[path]/[name of file to geocode].csv', encoding='latin1')

geolocator = Nominatim(user_agent='[input a unique identifier here, like an email address]')
# # 1 - function to delay between geocoding calls. Good for geocoding many physical addresses as the service provider can deny access 
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# # 2 - creates location column by applying the geocode that was just created
df['location'] = df['combined'].apply(geocode)

# # 3 - create longitude, laatitude and altitude from location column (returns tuple)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

# # 4 - split point column into latitude, longitude and altitude columns *this line will cause an error and will abort the program if any addresses fail to geocode* 
# make sure to only have successfully geocoded addresses in the target column before running this line
# df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)

df.to_csv('C:/[path]/[name of result file].csv')

print('Done')