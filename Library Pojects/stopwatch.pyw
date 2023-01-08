import time
import tkinter as tk
import datetime

root = tk.Tk()
root.title("Stopwatch")
root.geometry("600x400")
root.configure(bg="#363534")

start = 0
end = 0

# STOPWATCH DISPLAY
display = tk.Label(root,text="0:00:00.000000",font=("Arial",40),bg="#363534",fg="white")
display.place(x=120,y=100)

def time_display():
    global start_time
    global readable_time
    elapsed_time = time.time() - start_time
    readable_time = str(datetime.timedelta(seconds=elapsed_time))
    display.configure(text=readable_time)
    display.after_id = display.after(10,time_display)


# START BUTTON

def start_stopwatch():
    global start_time
    start_time = time.time()
    time_display()

start_button = tk.Button(root,text="Start",command=start_stopwatch,bg="#02f29e",fg="black",width=15,height=2,border=0)
start_button.place(x=150,y=250)

def end_stopwatch():
    display.after_cancel(display.after_id)
    display.configure(text=readable_time)

# STOP BUTTON

stop_button = tk.Button(root,text="Stop",command=end_stopwatch,bg="#2f3033",fg="white",width=15,height=2,border=0)
stop_button.place(x=325,y=250)

root.mainloop()