import phonenumbers
import opencage
import folium
from myphone import number


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)


from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key='bd18bf8c6a484476bc78e33e71d4052e'

geocoder=OpenCageGeocode(key)
query=str(location)
res=geocoder.geocode(query)
#print(res)

lat=res[0]['geometry']['lat']
lng=res[0]['geometry']['lng']

print(lat,lng)

myMap= folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("myPhLocation2.html")