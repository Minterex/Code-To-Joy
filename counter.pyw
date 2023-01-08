import tkinter as tk

root = tk.Tk()
root.title("Counter")
root.geometry("300x500")
root.configure(bg="#363534")

counter = 0

# FRAME

frame = tk.Frame(root,bg="#1e1e1f",width=280,height=480)
frame.place(x=10,y=10)

# HEADER

title = tk.Label(frame,text="Counter",font=("Bold",30),bg="#1e1e1f",fg="White")
title.place(x=65,y=40)

# COUNTER

counter_label = tk.Label(frame,text=counter, bg="#1e1e1f",fg="black", font=("Bold",50))
counter_label.place(x=140,y=160,anchor="center")

# BUTTONS

def add_counter():
    global counter
    counter += 1
    counter_label.configure(text=counter)

def sub_counter():
    global counter
    counter = counter - 1
    counter_label.configure(text=counter)

def reset_counter():
    global counter
    counter = 0
    counter_label.configure(text=counter)

add = tk.Button(frame,text="+",fg="black",bg="#02f29e",width=5,height=2,border=0,font=(20),command=add_counter)
add.place(x=50,y=300)

sub = tk.Button(frame,text="--",fg="black",bg="#02f29e",width=5,height=2,border=0,font=(40),command=sub_counter)
sub.place(x=180,y=300)

reset = tk.Button(frame,text="↻",fg="black",bg="#02f29e",width=5,height=2,border=0,font=(40),command=reset_counter)
reset.place(x=115,y=380)

root.mainloop()