from email.mime import image
import tkinter as tk
from turtle import color
import os


root = tk.Tk()
root.title("Code To Joy")
root.configure(bg="white")

header_label = tk.Label(root,text="Code-to-Joy",bg="white")
header_label.configure(font=('Times New Roman', 25))
header_label.place(x=320,y=20)

# Calc Codes
calc_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\calcicon.png")

calc_label = tk.Label(root, text="Calculator App")
calc_label.place(x=160,y=210)

def openFile():
        os.startfile(r"C:\Users\ACER\Code Projects\PyCharm\BasicCalculator\Calc.py")

calc_button = tk.Button(root,text="Open Calculator",image=calc_image,height="100",width="100",fg="black",command=openFile)
calc_button.place(x=150,y=100)

# Guessing Game Codes
gg_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\gameicon.png")

gg_label = tk.Label(root, text="Guessing Game")
gg_label.place(x=360,y=210)

def openFile2():
        os.startfile(r"C:\Users\ACER\Code Projects\PyCharm\Journey To Code\Guessing Game.py")

gg_button = tk.Button(root,text="Open Guessing Game",image=gg_image,height="100",width="100",fg="black",command=openFile2)
gg_button.place(x=350,y=100)

# Driving Quiz Codes
dq_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\quizicon.png")

drive_label = tk.Label(root,text="Driving Quiz")
drive_label.place(x=565,y=210)

def openFile3():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Driving quiz GUI.py")

drive_button = tk.Button(root,text="Open Driving Quiz",image=dq_image,height="0",width="0",fg="black",command=openFile3)
drive_button.place(x=550,y=100)

# Workspace Codes
ws_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\workicon.png")

workspace_label = tk.Label(root,text="Workspace")
workspace_label.place(x=168,y=385)

def openFile4():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Workspace.py")

workspace_button = tk.Button(root,text="Open Workspace",image=ws_image,height="0",width="0",fg="black",command=openFile4)
workspace_button.place(x=150,y=280)

# Old But Gold Codes
og_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\ogicon.png")

old_label = tk.Label(root,text="Old But Gold")
old_label.place(x=365,y=385)

def openFile5():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Old But Gold.py")

old_button = tk.Button(root,text="Open Old But Gold",image=og_image,height="0",width="0",fg="black",command=openFile5)
old_button.place(x=350,y=280)

# Drives Me Nutz
dmn_image = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\dmnicon.png")

dmn_label = tk.Label(root,text="Drives Me Nutz")
dmn_label.place(x=557,y=385)

def openFile6():
        os.startfile(r"C:\Users\ACER\Code Projects\VS Code\Drives Me Nutz.py")

dmn_button = tk.Button(root,text="Open Drives Me Nuts",image=dmn_image,height="0",width="0",fg="black",command=openFile6)
dmn_button.place(x=550,y=280)

root.geometry("800x500")

root.mainloop()