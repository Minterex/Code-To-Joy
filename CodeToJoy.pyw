from email.mime import image
import tkinter as tk
from turtle import color
import os
from tkinter import Scrollbar
import time


root = tk.Tk()
root.title("Code To Joy")
root.configure(bg="#1c1c1c")

frame = tk.Frame(root,bg="#272729",width=720,height=460)
frame.place(x=40,y=20)

# SCROLLWHEEL CODES

# create a canvas widget and place it inside the frame
canvas = tk.Canvas(frame, bg="#272729", bd=0, highlightthickness=0, width=720, height=460)
canvas.pack(side="left", fill="both", expand=True)
canvas.config(scrollregion=(0, 0, 1800, 600))

# create a scrollbar widget and place it on the right side of the frame
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=canvas.yview)

# set the yscrollcommand attribute of the canvas widget to the set method of the scrollbar widget
canvas.config(yscrollcommand=scrollbar.set)

# HEADER CODES
header_label = tk.Label(canvas,text="Code-to-Joy", bg="#272729", fg="white")
header_label.configure(font=('Comfortaa', 25))
header_label.place(x=312,y=37)

# CLOCK CODES

# create a label to display the time
time_label = tk.Label(canvas, font=("times", 15),bg="#272729",fg="white")
time_label.place(x=10,y=10)

# update the time every second
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.configure(text=current_time)
    time_label.after(1000, update_time)

update_time()

# CALCULATOR CODES
calc_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\calcicon.png")

calc_label = tk.Label(canvas, text="Calculator App", bg="#272729",fg="white")
calc_label.place(x=160,y=225)

def openFile():
        os.startfile(r"C:\Users\ACER\Code Projects\PyCharm\BasicCalculator\Calc.py")

calc_button = tk.Button(canvas,text="Open Calculator",image=calc_image,height="100",width="100",fg="black",border="0",command=openFile)
calc_button.place(x=150,y=115)

# GUESSING GAME CODES
gg_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\gameicon.png")

gg_label = tk.Label(canvas, text="Guessing Game",bg="#272729",fg="white")
gg_label.place(x=360,y=225)

def openFile2():
        os.startfile(r"C:\Users\ACER\Code Projects\PyCharm\Journey To Code\Guessing Game.py")

gg_button = tk.Button(canvas,text="Open Guessing Game",image=gg_image,height="100",width="100",fg="black",border="0",command=openFile2)
gg_button.place(x=350,y=115)

# DRIVING QUIZ CODES
dq_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\quizicon.png")

drive_label = tk.Label(canvas,text="Driving Quiz",bg="#272729",fg="white")
drive_label.place(x=565,y=225)

def openFile3():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Driving quiz GUI.py")

drive_button = tk.Button(canvas,text="Open Driving Quiz",image=dq_image,height="0",width="0",fg="black",command=openFile3)
drive_button.place(x=550,y=115)

# WORKSPACE APP CODES
ws_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\workicon.png")

workspace_label = tk.Label(canvas,text="Workspace",bg="#272729",fg="white")
workspace_label.place(x=168,y=400)

def openFile4():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Workspace.py")

workspace_button = tk.Button(canvas,text="Open Workspace",image=ws_image,height="0",width="0",fg="black",command=openFile4)
workspace_button.place(x=150,y=295)

# OLD BUT GOLD APP CODES
og_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\ogicon.png")

old_label = tk.Label(canvas,text="Old But Gold",bg="#272729",fg="white")
old_label.place(x=365,y=400)

def openFile5():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Old But Gold.py")

old_button = tk.Button(canvas,text="Open Old But Gold",image=og_image,height="0",width="0",fg="black",command=openFile5)
old_button.place(x=350,y=295)

# DRIVES ME NUTZ APP CODES
dmn_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\dmnicon.png")

dmn_label = tk.Label(canvas,text="Drives Me Nutz",bg="#272729",fg="white")
dmn_label.place(x=557,y=400)

def openFile6():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Drives Me Nutz.py")

dmn_button = tk.Button(canvas,text="Open Drives Me Nuts",image=dmn_image,height="0",width="0",fg="black",command=openFile6)
dmn_button.place(x=550,y=295)

# CANVAS WIDGETS CODES

# Placing all the widgets onto the canvas through windows as the ".place" code does not support scrollbars
time_label_window = canvas.create_window(365, 60, window=time_label)
header_label_window = canvas.create_window(365, 30, window=header_label)
calc_label_window = canvas.create_window(150, 220, window=calc_label)
calc_button_window = canvas.create_window(150, 155, window=calc_button)
gg_label_window = canvas.create_window(367, 220, window=gg_label)
gg_button_window = canvas.create_window(367, 155, window=gg_button)
drive_label_window = canvas.create_window(570, 220, window=drive_label)
drive_button_window = canvas.create_window(570, 155, window=drive_button)
workspace_label_window = canvas.create_window(150, 383, window=workspace_label)
workspace_button_window = canvas.create_window(150, 320, window=workspace_button)
old_label_window = canvas.create_window(367, 383, window=old_label)
old_button_window = canvas.create_window(367, 320, window=old_button)
dmn_label_window = canvas.create_window(570, 383, window=dmn_label)
dmn_button_window = canvas.create_window(570, 320, window=dmn_button)

# Make the scroll region of the scrollbar fit to all the widgets placed inside the canvas
canvas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.geometry("800x500")

root.mainloop()
