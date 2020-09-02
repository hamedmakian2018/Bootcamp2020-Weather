

from tkinter import *
import requests
from tkinter import messagebox
from PIL import ImageTk, Image


web = 'https://openweathermap.org/data/2.5/weather?q='
key = '&appid=439d4b804bc8187953eb36d2a8c26a02'
    
    

def get_weather(arg=None):

    def email():
                
        city_text = email_entry.get()
        
        print(city_text)
        app.destroy()





    city_text = city_entry.get()
    json_data = requests.get(web + city_text + key).json()
    try :
        longitude = json_data ['coord']['lon']
        longitude_entry.config(text=longitude)

        latitude = json_data ['coord']['lat']
        latitude_entry.config(text=latitude)

        state_weather = json_data ['weather'][0]['main']
        state_weather_entry.config(text=state_weather)


        des_weather = json_data ['weather'][0]['description']
        des_weather_entry.config(text=des_weather)

    


        temp = json_data ['main']['temp']
        temp_entry.config(text=temp)

        temp_min = json_data ['main']['temp_min']
        temp_min_entry.config(text=temp_min)




        temp_max = json_data ['main']['temp_max']
        temp_max_entry.config(text=temp_max)


        pressure = json_data ['main']['pressure']
        pressure_entry.config(text=pressure)

        humidity = json_data ['main']['humidity']
        humidity_entry.config(text=humidity)

        wind_speed = json_data ['wind']['speed']
        wind_speed_entry.config(text=wind_speed)

        clouds = json_data ['clouds']['all']
        clouds_entry.config(text=clouds)

        country = json_data ['sys']['country']
        country_entry.config(text=country)

        city_name = json_data ['name']
        city_name_entry.config(text=city_name)

        icon = json_data ['weather'][0]['icon']
        icon_entry.config(text=icon)
        
        #addr="E:\MMM\Weather\image\\"
        #image['bitmap']= addr+icon+".png"
        pic="Image\\"+icon+".png"
        
        img1=PhotoImage(file= pic)
        w1= Label(app,image=img1)
        w1.image=img1
        w1.place(x=150,y=270)

        #canvas = Canvas(app, width = 100, height = 100)  
        #w1=canvas.place(x=150,y=270)
        #pic=addr+icon+".png"
        #print(pic)
        #img = ImageTk.PhotoImage(Image.open(pic))  
        #canvas.create_image(0, 0, anchor=NW, image=img)

        l1= '*Your city is '+city_name+ ' in '+ country+'*\n ' 
        l2='*Coordination of '+city_name+ ' is : Latitude: '+ str(latitude) + ' , Langtitude: '+ str(longitude)+'.\n' 
        l3='State of weather is '+des_weather+'.\n'
        l4='Temperature of '+city_name+ ' is '+str(temp)+ ' degree celsius.\n' 
        l4_1= 'Minimum tepmerature is ' + str(temp_min)+ ' degree celsius'
        l4_2= 'and maximun temperatue is '+str(temp_max)+' degree celsius.\n'
        l5='The humidity value of'+city_name+ ' is : '+str(humidity)+'.\n'
        l6='The pressure value of '+city_name+ ' is : '+str(pressure)+'.\n'
        l7='The clouds value of '+city_name+ ' is : '+str(clouds)+' and speed of wind is '+str(wind_speed)+' m/s.'
        destotal= l1+l2+l3+l4+l4_1+l4_2+l5+l6+l7
        destotal_entry.config(text=destotal)
        #print(destotal)
        #window = tk.Toplevel(app)
        #window.grab_set()
        
        user_lb =Label(app, text='Do you want this information in you email', font=('bold',10))
        user_lb.place(x=30,y=560)

        user_lb =Label(app, text='Please enter your email', font=('bold',10))
        user_lb.place(x=30,y=590)
        
        
        email_entry = Entry (app, width=15, font=('bold',20))
        email_entry.focus()
        email_entry.bind("<Button-1>",email)
        email_entry.place(x=300,y=580)


        





        send_btn = Button(app, text='Send ', width=10, font=('bold',10), command=email).place(x=30,y=620)
        cancel_btn = Button(app, text='Cancel ', width=10, font=('bold',10), command=app.destroy)
        cancel_btn.place(x=200,y=620)
    










  
             
    except KeyError:
        longitude_entry.config(text="")
        latitude_entry.config(text="")
        state_weather_entry.config(text="")
        des_weather_entry.config(text="")
        temp_entry.config(text="")
        temp_min_entry.config(text="")
        temp_max_entry.config(text="")
        pressure_entry.config(text="")
        humidity_entry.config(text="")
        wind_speed_entry.config(text="")
        clouds_entry.config(text="")
        country_entry.config(text="")
        city_name_entry.config(text="")
        icon_entry.config(text="")
        destotal_entry.config(text="")

        img1=PhotoImage(file= "Image\\nothing.png")
        w1= Label(app,image=img1)
        w1.place(x=150,y=270)




        messagebox.showerror('Error','Cannot find city '+city_text)

        
app = Tk()
app.title('Weather Application')
app.geometry('650x700')
app.configure(background = "light green") 

location_lbl =Label(app, text='City ,Country Postal Abbreviation', font=('bold',10)).place(x=10,y=10)
location_lbl2 =Label(app, text= 'like: Helsinki, FI', font=('bold',10)).place(x=40,y=30)
city_entry = Entry (app, width=15, font=('bold',20))
city_entry.focus()
city_entry.bind("<Return>",get_weather)
city_entry.place(x=220,y=10)


search_btn = Button(app, text='Search ', width=20, font=('bold',10), command=get_weather).place(x=470,y=15)




country_lbl =Label(app, text='Country', width=15, font=('bold',10)).place(x=10,y=60)
country_entry = Label (app,width=15, font=('bold',10))
country_entry.place(x=160,y=60)

city_name_lbl =Label(app, text='City',width=15, font=('bold',10)).place(x=350,y=60)
city_name_entry = Label (app,width=15, font=('bold',10))
city_name_entry.place(x=500,y=60)



latitude_lbl =Label(app, text='Latitude', width=15, font=('bold',10)).place(x=350,y=90)
latitude_entry = Label (app, text = "",width=15, font=('bold',10))
latitude_entry.place(x=500,y=90)

langitude_lbl =Label(app, text='Longitude', width=15, font=('bold',10)).place(x=10,y=90)
longitude_entry = Label (app, text = "",width=15, font=('bold',10))
longitude_entry.place(x=160,y=90)



state_weather_lbl =Label(app, text='State_weather', width=15, font=('bold',10)).place(x=350,y=120)
state_weather_entry = Label (app,text='',width=15, font=('bold',10))
state_weather_entry.place(x=500,y=120)


temp_lbl =Label(app, text='Temperature', width=15, font=('bold',10)).place(x=10,y=120)
temp_entry = Label (app,text='',width=15, font=('bold',10))
temp_entry.place(x=160,y=120)


temp_min_lbl =Label(app, text='Temperature Min', width=15, font=('bold',10)).place(x=10,y=150)
temp_min_entry = Label (app,text='',width=15, font=('bold',10))
temp_min_entry.place(x=160,y=150)

temp_max_lbl =Label(app, text='Temperature Max', width=15, font=('bold',10)).place(x=350,y=150)
temp_max_entry = Label (app,text='',width=15, font=('bold',10))
temp_max_entry.place(x=500,y=150)



pressure_lbl =Label(app, text='Pressure', width=15, font=('bold',10)).place(x=10,y=180)
pressure_entry = Label (app,text='',width=15, font=('bold',10))
pressure_entry.place(x=160,y=180)

humidity_lbl =Label(app, text='Humidity', width=15, font=('bold',10)).place(x=350,y=180)
humidity_entry = Label (app,text='',width=15, font=('bold',10))
humidity_entry.place(x=500,y=180)




wind_speed_lbl =Label(app, text='Wind Speed', width=15, font=('bold',10)).place(x=10,y=210)
wind_speed_entry = Label (app,text='',width=15, font=('bold',10))
wind_speed_entry.place(x=160,y=210)

clouds_lbl =Label(app, text='Clouds', width=15, font=('bold',10)).place(x=350,y=210)
clouds_entry = Label (app,text='',width=15, font=('bold',10))
clouds_entry.place(x=500,y=210)

des_weather_lbl =Label(app, text='Description', width=15, font=('bold',10)).place(x=10,y=240)
des_weather_entry = Label (app,text='',width=50, font=('bold',10))
des_weather_entry.place(x=160,y=240)

icon_lbl =Label(app, text='Icon', width=15, font=('bold',10)).place(x=10,y=270)
icon_entry = Label (app,text='',width=10, font=('bold',10))
icon_entry.place(x=160,y=270)
#image = Label(app, bitmap='')
#image.place(x=150,y=270)
temp_lbl = Label(app, text='temperature')
#temp_lbl.pack()
weather_lbl = Label(app, text='weather')
#weather_lbl.pack()
#addr2="E:\MMM\Weather\image\\"
#image = Image.open("E:\MMM\Weather\image\Bootcamp.png")
# The (450, 350) is (height, width)
#image = image.resize((200, 132), Image.ANTIALIAS)
#my_img = ImageTk.PhotoImage(image)
#my_img = Label(image = my_img).place(x=400,y=270)
        
img2=PhotoImage(file= "Image\\Bootcamp1.png")
w2= Label(app,image=img2).place(x=400,y=270)

dedestotal_lbl =Label(app, text='Description in text', width=15, font=('bold',10)).place(x=10,y=240)
destotal_entry = Label (app,text='',width=70, height= 10, font=('bold',10))
destotal_entry.place(x=30,y=380)







app.mainloop()