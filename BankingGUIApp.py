#imports
import tkinter
import _tkinter
import os 
from PIL import ImageTk, Image


HEIGHT = 150
WIDTH = 150
#main Screen
root = tkinter.Tk()
root.title("Banking App")

canvas = tkinter.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

frame = tkinter.Frame(root, bg='red')
frame.pack()

root.mainloop()

#image Imports 
img = Image.open('secure1.png')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(root, text ="Abhishek Banking App",font =('Calibri',14)).grid(row = 0,sticky = N,pady = 10)   