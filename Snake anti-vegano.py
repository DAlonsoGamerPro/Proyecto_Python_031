from tkinter import Tk, Frame, Canvas, Button, Label, IntVar, ALL
import random
from pygame import mixer

root = Tk()
root.config(bg="gray41")
root.title("Snake, Snake? SNAKEEEEEEE")
root.geometry("485x510")
root.resizable(0,0)

frame_1 = Frame(root, width = 485, height = 25, bg = "gray41")
frame_1.grid(column = 0, row = 0)
frame_2 = Frame(root,width = 485, height = 490, bg = "gray42")
frame_2.grid(column = 0, row = 1)

canvas = Canvas(frame_2, bg = "blue", width = 479, height = 479)
canvas.pack()

for i in range(0,460,30):
    for j in range(0,460,30):
        canvas.create_rectangle(i, j, i + 30, j + 30, fill = "black", outline = "blue")
        
canvas.create_text(75,75, text = "🥩", fill = "red", font = ("Arial", 18), tag = "food")

btn1 = Button(frame_1, text = "Salir", bg = "pink")
btn1.grid(column = 0, row = 0, padx = 20)

btn2 = Button(frame_1, text = "Iniciar", bg = "red")
btn2.grid(column = 1, row = 0, padx = 20)

cantidad = Label(frame_1, text = "Cantidad 🥩:  ", bg = "gray41", fg = "orange", font = ("Arial", 12, "bold"))
cantidad.grid(column = 2, row = 0, padx = 20)

root.mainloop()