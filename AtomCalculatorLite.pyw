import tkinter as tk

root = tk.Tk()
root.title("Atom Calculator")
root.geometry("500x600")
root.configure(bg="#202121")

# FRAME FOR NUMBER DISPLAY

display_frame = tk.Frame(root, width=500,height=170,bg="#1e1e1f")
display_frame.place(x=0 ,y=0)

# NUMBER DISPLAY
display = tk.Entry(root,width=500,bg="#323333")
display.place(x=0,y=10)

# FUNCTIONS OF EACH BUTTON

def number_buttons(num):
    current_display = display.get()
    display.delete(0, tk.END)
    display.insert(0,str(current_display)+str(num))

def clear_button():
   display.delete(0, tk.END)

def add_button():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    display.delete(0, tk.END)

def sub_button():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "subtraction"
    display.delete(0, tk.END)

def multi_button():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "multiplication"
    display.delete(0, tk.END)

def divide_button():
    first_number = display.get()
    global f_num
    f_num = int(first_number)
    global math
    math = "division"
    display.delete(0, tk.END)

def equal_button():
    second_number = display.get()
    display.delete(0, tk.END)
    if math == "addition":
        display.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        display.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        display.insert(0, f_num * int(second_number))
    elif math == "division":
        display.insert(0, f_num / int(second_number))

# Create the buttons for the calculator
button_1 = tk.Button(root, text="1", width=10, bg="#21519e", fg="white", border="0", command=lambda: number_buttons(1))
button_1.place(x=116,y=390)
button_2 = tk.Button(root, text="2", width=10,bg="#21519e", fg="white", border="0", command=lambda: number_buttons(2))
button_2.place(x=206,y=390)
button_3 = tk.Button(root, text="3", width=10,bg="#21519e", fg="white",border="0",  command=lambda: number_buttons(3))
button_3.place(x=296,y=390)
button_4 = tk.Button(root, text="4", width=10,bg="#21519e", fg="white", border="0", command=lambda: number_buttons(4))
button_4.place(x=116,y=420)
button_5 = tk.Button(root, text="5", width=10,bg="#21519e", fg="white", border="0", command=lambda: number_buttons(5))
button_5.place(x=206,y=420)
button_6 = tk.Button(root, text="6", width=10,bg="#21519e", fg="white",border="0", command=lambda: number_buttons(6))
button_6.place(x=296,y=420)
button_7 = tk.Button(root, text="7", width=10,bg="#21519e", fg="white",border="0",  command=lambda: number_buttons(7))
button_7.place(x=116,y=450)
button_8 = tk.Button(root, text="8", width=10, bg="#21519e", fg="white",border="0", command=lambda: number_buttons(8))
button_8.place(x=206,y=450)
button_9 = tk.Button(root, text="9", width=10,bg="#21519e", fg="white", border="0", command=lambda: number_buttons(9))
button_9.place(x=296,y=450)
button_0 = tk.Button(root, text="0", width=10,bg="#21519e", fg="white", border="0", command=lambda: number_buttons(0))
button_0.place(x=206,y=480)
add = tk.Button(root, text="+", width=5, height=2,bg="#21519e", fg="white", border="0", command=add_button)
add.place(x=174,y=240)
equal = tk.Button(root, text="=", width=5,height=2,bg="#21519e", fg="white",border="0",  command=equal_button)
equal.place(x=222,y=240)
clear = tk.Button(root, text="Clear",width=5,bg="#21519e", fg="white",border="0", command=clear_button)
clear.place(x=222,y=555)
multi = tk.Button(root, text="X",width=5,height=2,bg="#21519e", fg="white",border="0", command=multi_button)
multi.place(x=270,y=240)
divide = tk.Button(root, text="/",width=5,height=2,bg="#21519e", fg="white",border="0", command=divide_button)
divide.place(x=222,y=195)
sub = tk.Button(root, text="-",width=5,height=2,bg="#21519e", fg="white",border="0",  command=sub_button)
sub.place(x=222,y=285)

root.mainloop()