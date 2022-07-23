import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'ea4c8d1b27214a539d849f8b7122d292'

geocoder = OpenCageGeocode(key)
query = str(location)
results =  geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start= 5)

n = 0
max_con = 0
for x in results:
    max_con = results[n]['confidence']
    if(results[n]['confidence'] >= 5):
        folium.Marker([results[n]['geometry']['lat'],results[n]['geometry']['lng']], popup=max_con).add_to(myMap)
    n += 1
print(n)

myMap.save("mylocation.html")