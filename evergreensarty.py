
mortarposy = 0
mortarposhor = 0
targetposy = 0
targetposx = 0
from tkinter import *
import time
import math
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog
mills = 0.16
minus = 1











root = Tk()
root.title('Evergreen#2723 Frontlines Arty Calculator')
root.resizable(False, False)

w = Canvas(root, width=900, height=500)

bro = Image.open("peter.png")

def mapselectpeters():
    global bro
    global minus
    global mills
    minus = 1
    mills = 0.25
    original = Image.open("peter.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack
    minus = 1



def mapselectmar():
    global bro
    global minus
    global mills
    minus = 4
    mills = 0.25
    original = Image.open("mar.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack


def mapselectmansion():
    global bro
    global minus
    global mills
    minus = 4
    mills = 0.225
    original = Image.open("mansion.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack



def mapselectfre():
    global minus
    global mills
    minus = 4
    mills = 0.25
    global bro
    original = Image.open("fre.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack


def mapselectwaste():
    global minus
    global mills
    minus = 1
    mills = 0.16
    global bro
    original = Image.open("waste.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack




def mapselectfox():
    global minus
    global mills
    minus = 1
    mills = 0.16
    global bro
    original = Image.open("fox.png")
    original = original.resize((880,500)) #resize image
    img2 = ImageTk.PhotoImage(original) 
    bro = w.create_image(0, 0, image=img2, anchor="nw")
    bro.pack







b12 = Button(root, text="Peters",
            command=lambda m="peters": mapselectpeters())
quit_button_window2 = w.create_window(600, 457, anchor='nw', window=b12)    

b122 = Button(root, text="Wasteland",
            command=lambda m="Wasteland": mapselectwaste())
quit_button_window22 = w.create_window(700, 457, anchor='nw', window=b122)    


b1222 = Button(root, text="Freurlund",
            command=lambda m="Freurlund": mapselectfre())
quit_button_window222 = w.create_window(800, 457, anchor='nw', window=b1222)    
   

b1222222 = Button(root, text="Mansion",
            command=lambda m="Mansion": mapselectmansion())
quit_button_window2222222 = w.create_window(500, 457, anchor='nw', window=b1222222)    
   

b12222 = Button(root, text="Foxhole",
            command=lambda m="Foxhole": mapselectfox())
quit_button_window2222 = w.create_window(400, 457, anchor='nw', window=b12222)    
   

b122222 = Button(root, text="Marre",
            command=lambda m="Marre": mapselectmar())
quit_button_window22222 = w.create_window(300, 457, anchor='nw', window=b122222)    
   



def distancecalc():
    global targetposx
    global targetposy
    global mortarposhor
    global mortarposy

    return math.sqrt((abs(mortarposhor/25-targetposx/25))**2+(abs(mortarposhor/25-targetposx/25))**2)
##ef ##myround(x, base=1):
    ##return base * round(x/base)
def calculate():
    print(str(  5-((distancecalc()-minus)*mills)))
    tkinter.messagebox.showinfo("Answer", str(  5-((distancecalc()-minus)*mills)))

    

    #setting up a tkinter canvas
b1 = Button(root, text="calculate",
            command=lambda m="calculating": calculate())
quit_button_window = w.create_window(10, 10, anchor='nw', window=b1)    
   
#adding the image





    
def leftclick(event2):
    global img
    global mortarposy
    global mortarposhor
    x, y = event2.widget.winfo_pointerxy()
    print('{}, {}'.format(x, y))
    mortarposhor = x
    mortarposy = y
    print(mortarposy)
    print("completed")
    



def rightclick(event2):
    global img3
    global targetposx
    global targetposy
    x, y = event2.widget.winfo_pointerxy()
    print('{}, {}'.format(x, y))
    targetposx = x
    targetposy = y
    print("completed")
    



w.bind("<Button-1>", leftclick)

w.bind("<Button-3>", rightclick)


w.pack()
w.mainloop()

def newround():
    print("hi")




w.pack()

           
    
            


##ef mortarvals():


