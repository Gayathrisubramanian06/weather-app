from tkinter import *                                    # for GUI
from tkinter import ttk                          
win = Tk()                                             # window is created
win.title("Weather App")    
win.config(bg = "lightblue")
win.geometry("500x500")

name_label = Label(win, text="Weather App",font=('Arial', 20, 'bold'))  
name_label.place(x=160,y=20, height=50, width=200)

list_name=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir",
    "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Delhi", "Puducherry", "Ladakh"
]   

com=ttk.Combobox(win,text="WEATHER APP",values=list_name,font=('Arial', 20, 'bold'))   # box where city names r entered
com.place(x=50,y=100, height=50, width=400)

done_button = Button()

win.mainloop()                             # window continues until user interacts  