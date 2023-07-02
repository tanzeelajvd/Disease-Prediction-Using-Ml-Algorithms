from tkinter import *
from tkinter import messagebox as tkMessageBox
import urllib.request
import json,webbrowser,ctypes
def button_click_function():
    window.destroy()
    exec(open("azure_diabetic.py").read())
def button_click_function2():
    webbrowser.open("http://www.webmd.com/diabetes/tc/criteria-for-diagnosing-diabetes-topic-overview")

window = Tk()
window.geometry("500x415")
window.title("DIABETES DIAGONOSTIC APP")
window.resizable(width=False, height= False)

igm = PhotoImage(file="givee.gif")
btnshow = Button(window ,image=igm, command=button_click_function)

btnshow.pack()


igsm = PhotoImage(file="visitt.gif")
btnshow1 = Button(window ,image=igsm, command=button_click_function2)

btnshow1.pack()
window.mainloop()
