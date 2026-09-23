from tkinter import *             # for GUI
from tkinter import ttk           # imported separately to access widgets inside ttk   

import requests

try:
    from config import API_KEY
except ImportError:
    API_KEY = "YOUR_API_KEY_HERE"

def data_get():
    city = city_name.get().strip()
    if not city:
        return
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}").json()
    if data.get("cod") == 200:
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])                       # data is given in dictionary format
        temp_label1.config(text=str(int(data["main"]["temp"] - 273.15)) + "°C")        # maps corresponding values in dict to defined variables
        press_label1.config(text=str(data["main"]["pressure"]))
    else:
        w_label1.config(text="Error")
        wb_label1.config(text=data.get("message", "Not found"))
        temp_label1.config(text="")
        press_label1.config(text="")



win = Tk()                        # simple window is created
win.title("Weather App")    
win.config(bg = "lightblue")
win.geometry("500x500")

name_label = Label(win, text="Weather App",font=('Arial', 20, 'bold'))  
name_label.place(x=160,y=20, height=50, width=200)

city_name=StringVar()

list_name=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Delhi", "Puducherry", "Ladakh" ]   

com=ttk.Combobox(win,text="WEATHER APP",values=list_name,font=('Arial', 20, 'bold'),textvariable=city_name)  # box where city names r entered
com.place(x=50,y=100, height=50, width=400)          #ttk=Tkinter themed widgets


w_label = Label(win, text="Weather Climate",font=('Arial', 10, 'bold'))  
w_label.place(x=10,y=320, height=15, width=150)

w_label1 = Label(win, text="",font=('Arial', 10, 'bold'))  
w_label1.place(x=170,y=320, height=15, width=150)                    # x=width of original label (for displaying actual value)

wb_label = Label(win, text="Weather Description",font=('Arial', 10, 'bold'))  
wb_label.place(x=10,y=350, height=15, width=150)

wb_label1 = Label(win, text="",font=('Arial', 10, 'bold'))  
wb_label1.place(x=170,y=350, height=15, width=150)

temp_label = Label(win, text="Temperature",font=('Arial', 10, 'bold'))  
temp_label.place(x=10,y=380, height=15, width=150)

temp_label1 = Label(win, text="",font=('Arial', 10, 'bold'))  
temp_label1.place(x=170,y=380, height=15, width=150)

press_label = Label(win, text="Pressure",font=('Arial', 10, 'bold'))  
press_label.place(x=10,y=410, height=15, width=150)

press_label1 = Label(win, text="",font=('Arial', 10, 'bold'))  
press_label1.place(x=170,y=410, height=15, width=150)

done_button = Button(win,text="Done",font=('Arial', 15,'bold'),command=data_get) 
done_button.place(x=220,y=180)


win.mainloop()                             # window continues until user interacts  

