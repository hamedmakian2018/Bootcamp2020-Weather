import requests

web = 'https://openweathermap.org/data/2.5/weather?q='
key = '&appid=439d4b804bc8187953eb36d2a8c26a02'
city = input ("City ,Country Postal Abbreviation \nlike: Helsinki, FI \n")    
url = web+city+key    

json_data = requests.get(url).json()
latitude = str(json_data ['coord']['lat'])
langitude = str(json_data ['coord']['lon'])




state_weather = json_data ['weather'][0]['main']

des_weather = json_data ['weather'][0]['description']
icon = json_data ['weather'][0]['icon']
temp = str(json_data ['main']['temp'])
temp_min = str(json_data ['main']['temp_min'])
temp_max = str(json_data ['main']['temp_max'])
pressure = str(json_data ['main']['pressure'])
humidity = str(json_data ['main']['humidity'])
wind_speed = str(json_data ['wind']['speed'])
clouds = str(json_data ['clouds']['all'])
country = json_data ['sys']['country']
city_name = json_data ['name']

print ('Your city is '+city_name+ ' in '+ country+'.')
print ('Coordination of city is : Latitude: '+ latitude + ' , Langtitude: '+ langitude+'.')
print ('State of weather is '+des_weather+'.')
print ('Temperature of city is '+temp+ ' degree celsius. Minimum tepmerature is ' + temp_min+ ' degree celsius and maximun temperatue is '+temp_max+' degree celsius.' )
print ('The humidity value of city is : '+humidity+'.')
print ('The pressure value of city is : '+pressure+'.')
print ('The clouds value of city is : '+clouds+' and speed of wind is '+wind_speed+' m/s.')
city = input ("Press Enter key to exit\n \n \n")  






l1= '*Your city is '+city_name+ ' in '+ country+'*\n ' 
l2='*Coordination of '+city_name+ ' is : Latitude: '+ latitude + ' , Langtitude: '+ langitude+'.\n' 
l3='State of weather is '+des_weather+'.\n'
l4='Temperature of '+city_name+ ' is '+temp+ ' degree celsius. Minimum tepmerature is ' + temp_min+ ' degree celsius and maximun temperatue is '+temp_max+' degree celsius.\n'
l5='The humidity value of'+city_name+ ' is : '+humidity+'.\n'
l6='The pressure value of '+city_name+ ' is : '+pressure+'.\n'
l7='The clouds value of '+city_name+ ' is : '+clouds+' and speed of wind is '+wind_speed+' m/s.'

print (l1+l2+l3+l4+l5+l6+l7)
city = input ("Press Enter key to exit")  

