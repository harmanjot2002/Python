#Weight-Converter GUI
#Let's Create a GUI-based convertor that accepts a kilogram input value and converts that value to grams,pounds,and ounces when the user clicks the convert button.
#We don't need to install any package in our system to run this script.Because we craeye our own GUI with the help of tkinter.Tkinter is automatically provided by the python while installing.
#Tkinter package(Tk interface) is the standard Python interface to the Tcl/Tk GUI toolkit.Both Tk and tkinter are available on most Unix platforms,including macOs,as well as on Windows systems.
#pack() helps to display widgets on GUI window.

#Steps:
#1.Importing required modules:
import tkinter as tk
from tkinter import *


#2.Creating GUI:
window=Tk() #Creating a window
window.title("PythonGeeks") #Title of a window
window.geometry("500x500") #geometry of window
Label(window,text="WEIGHT CONVERTOR",font=("Arial",20),bg="black",fg="yellow").pack() #Create a label

kg=tk.IntVar() #kg is integer type

#3.Coversion to Grams,Ounce and Pound:
def convert_to_gram():
    kg1=kg.get() #getting the value
    gram=float(kg1)*1000 #Convert to float
    Label(window,text="This weight in grams would be ",font=("Arial",12)).pack()
    Label(window,text=gram,bg="red").pack()

def convert_to_ounce():
    kg1=kg.get() #getting the value
    ounce=float(kg1)*35.274 #Convert to float
    Label(window,text="This weight in ounce would be ",font=("Arial",12)).pack()
    Label(window,text=ounce,bg="red").pack()

def convert_to_pound():
    kg1=kg.get() #getting the value
    pound=float(kg1)*2.20462 #Convert to float
    Label(window,text="This weight in pound would be ",font=("Arial",12)).pack()
    Label(window,text=pound,bg="red").pack()
    
Label(window,text="Enter the weight in Kgs",font=("Arial",14)).pack()

Entry(window,textvariable=kg).pack()#Entry field 

#Creating Buttons
Button(window,text="Convert to Gram",bg="blue",command=convert_to_gram).pack()
Button(window,text="Convert to Ounce",bg="blue",command=convert_to_ounce).pack()
Button(window,text="Convert to Pound",bg="blue",command=convert_to_pound).pack()

window.mainloop()