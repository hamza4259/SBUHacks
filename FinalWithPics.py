import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import Tk, Canvas, Frame, BOTH
from main import mainStructure
from PIL import ImageTk,Image
from time import sleep
from mapIt import getDirections

#LOADING SCREEN START

def task():
    # The window will stay open until this function call ends.
    sleep(1)
    loading.destroy()

loading = tk.Tk()
loading.title("Welcome to Hospital Locator")

C = Canvas(loading, bg="blue", height=250, width=300)
filename = PhotoImage(file = "images/Frame-2.png")
background_label = Label(loading, image=filename)
loading.geometry('1280x820')
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
loading.after(100, task)
loading.mainloop()

#LOADING SCREEN END
#print("Loading loop is now over and we can do other stuff.")


#MAIN WINDOW START

# create window
window = Tk()
window.title("SquishySquids App")
# setting window size
window.geometry('1280x820')
w = Canvas(window, width = 1280, height = 820)
w.pack()

#MAIN WINDOW END



# COMPONENTS START

# create a label widget with font size
#lbl = Label(window, text = "Hospitals Near You", font = ("Arial Bold",20))
#lbl.grid(column = 0, row = 5)

#LEFT SIDE BANNER
def drawLeft():
    y = int(820 / 2)
    w.create_line(0, y, 1280, y, fill="#303941")

    #Blue Background
    w.create_rectangle(0, 0, 450, 820, outline="#BADEFF", fill="#BADEFF", width=2)
    #The line
    w.create_line(50, 150, 400, 150, fill="#476042")
    #Hospitals Near You
    mylabel = w.create_text((220, 100), text="Hospitals Near You", font = ("Montserrat 25 bold"))
    #Address 1
    shortAddressIWillUseInThisUI = mainStructure()
    mylabel = w.create_text((220, 185), text=shortAddressIWillUseInThisUI[0], font = ("Montserrat 16 bold"))
    mylabel2 = w.create_text((220, 225), text="Closest To You!!!", font = ("Montserrat 16 bold"))
    #Address 2
    print(shortAddressIWillUseInThisUI[0])
    shortAddressIWillUseInThisUI = mainStructure()
    mylabel = w.create_text((220, 285), text=shortAddressIWillUseInThisUI[1], font = ("Montserrat 16 bold"))
    w.create_line(50, 250, 400, 250, fill="#476042")
    #Address 3
    shortAddressIWillUseInThisUI = mainStructure()
    mylabel = w.create_text((220, 385), text=shortAddressIWillUseInThisUI[2], font = ("Montserrat 16 bold"))
    w.create_line(50, 350, 400, 350, fill="#476042")
    #Address 4
    shortAddressIWillUseInThisUI = mainStructure()
    mylabel = w.create_text((220, 485), text=shortAddressIWillUseInThisUI[3], font = ("Montserrat 16 bold"))
    w.create_line(50, 450, 400, 450, fill="#476042")
    #Address 5
    shortAddressIWillUseInThisUI = mainStructure()
    mylabel = w.create_text((220, 585), text=shortAddressIWillUseInThisUI[4], font = ("Montserrat 16 bold"))
    w.create_line(50, 550, 400, 550, fill="#476042")
    w.create_line(50, 620, 400, 620, fill="#476042")
    #bottom stuff
    mylabel = w.create_text((220, 700), text="In Case of An Emergency, Call 911", font = ("Montserrat 18 bold"))

    b = Canvas(window, width = 1280, height = 820)
    b.pack()
    
    button = Button(b, text = 'Open Map', command = getDirections())  
    button.pack()  
    #print('Left DONE')


drawLeft()

map1 = Image.open("images/Map1.png")
map1 = map1.resize((830, 410), Image.ANTIALIAS)
map1 = ImageTk.PhotoImage(map1)

map2 = Image.open("images/Map2.png")
map2 = map2.resize((830, 410), Image.ANTIALIAS)
map2 = ImageTk.PhotoImage(map2)

def drawRight():            
    w.create_image(450, 0, anchor=NW, image=map1)
    w.create_image(450, 410, anchor=NW, image=map2)
    w.create_line(450, 410, 1280, 410, fill="#303941")


drawRight()


#index = open("search.html").read().format(address = shortAddressIWillUseInThisUI[0][0], time =shortAddressIWillUseInThisUI[0][2], distance = shortAddressIWillUseInThisUI[0][1] )
#webbrowser.open("Search.html")


# PROBABLY THE MOST IMPORTANT PART!!!!!!!!!!
# if you forget to call the mainloop function, nothing will appear to the user
window.mainloop()

