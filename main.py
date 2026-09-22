from tkinter import *                             # for GUI
win = Tk()                                             # window is created
win.title("Weather App")    
win.config(bg = "lightblue")
win.geometry("500x500")

name_label = Label(win, text="Weather App",font=('Arial', 20, 'bold'))  

name_label.place(x=50,y=50, height=50, width=400)
win.mainloop()                               # window continues until user interacts