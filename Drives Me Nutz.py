import tkinter as tk
import os
from tkinter.font import BOLD

root = tk.Tk()
root.geometry("700x550")
root.configure(bg="black")
root.title("Drives Me Nutz")

# Instructions & welcome
logo = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\drivelogo.png")
logo_label = tk.Label(root,image=logo,borderwidth=0)
logo_label.place(x=190,y=105)

instruction_label = tk.Label(root,text="Select a course to review",fg="white",bg="black")
instruction_label.place(x=250,y=350)
instruction_label.configure(font=("Calibri",15,BOLD))

# Button Functions

def rules():

    def home():
        root.geometry("700x550")
        rule_txt.destroy()
        rulesimage_label.destroy()
        back.destroy()
        global logo
        global rule_btn
        global eti_btn
        global tip_btn
        global logo_label
        global instruction_label
        logo = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\drivelogo.png")
        logo_label = tk.Label(root,image=logo,borderwidth=0)
        logo_label.place(x=190,y=105)

        instruction_label = tk.Label(root,text="Select a course to review",fg="white",bg="black")
        instruction_label.place(x=250,y=350)
        instruction_label.configure(font=("Calibri",15,BOLD))
        rule_btn = tk.Button(root,text="Rules",fg="black",bg="white",height=2,width=10,command=rules)
        rule_btn.place(x=100,y=450)

        eti_btn = tk.Button(root,text="Etiquettes",fg="black",bg="white",height=2,width=10,command=eti)
        eti_btn.place(x=325,y=450)

        tip_btn = tk.Button(root,text="Tips",fg="black",bg="white",height=2,width=10,command=tips)
        tip_btn.place(x=540,y=450)


    logo_label.destroy()
    instruction_label.destroy()
    rule_btn.destroy()
    eti_btn.destroy()
    tip_btn.destroy()
    root.geometry("1000x500")
    rule_txt = tk.Text(root,bg="black",fg="white",borderwidth=0,width=71)
    rule_txt.place(x=50,y=80)
    therules = """First things first, remember that drivers should be on the left-hand side of the road in Indonesia. Drivers must also carry a valid and certified SIM licence. However, foreigners are permitted to use international driving licence, along with their home country licence. If you are a foreigner who plans on living in Indonesia, we suggest you get a SIM licence. All these documents should then be accompanied with the vehicle's registration papers at all times. If your car is a rental, then you must have the rental papers available on you.\n\nFor safety, the rules state that all passengers riding on the front seats of the car must utilize seat belts. However, it is not mandatory for the back seat passengers. You might even find that most Indonesian cars do not have seat belts at the back. For motorcycles, you are limited to only one driver and one passenger on the vehicle. Both should be wearing helmets which meet the minimum legal standards. Mobile phones are also highly prohibited to be used by the drivers while driving simultaneously. This is to avoid any accidents. To avoid even more accidents, it is a rule for all drivers to signal using their blinkers before turning left or right. Of course, these are just some specific rules. You must still follow all the other common rules, such as not driving while drunk, even if they are not mentioned.\nhttps://www.angloinfo.com/how-to/indonesia/transport/driving/rules-regulations"""
    rule_txt.insert(tk.END,therules)
    global rulesimage
    rulesimage = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\trafficrules.png")
    rulesimage_label = tk.Label(root,image=rulesimage,borderwidth=0,bg="black",fg="black")
    rulesimage_label.place(x=650,y=120)
    back = tk.Button(root,text="<- Back",fg="black",bg="white",command=home)
    back.place(x=1,y=1)

def eti():

    def home():
        root.geometry("700x550")
        back.destroy()
        eti_txt.destroy()
        overtake_label.destroy()
        global logo
        global rule_btn
        global eti_btn
        global tip_btn
        global logo_label
        global instruction_label
        logo = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\drivelogo.png")
        logo_label = tk.Label(root,image=logo,borderwidth=0)
        logo_label.place(x=190,y=105)

        instruction_label = tk.Label(root,text="Select a course to review",fg="white",bg="black")
        instruction_label.place(x=250,y=350)
        instruction_label.configure(font=("Calibri",15,BOLD))
        rule_btn = tk.Button(root,text="Rules",fg="black",bg="white",height=2,width=10,command=rules)
        rule_btn.place(x=100,y=450)

        eti_btn = tk.Button(root,text="Etiquettes",fg="black",bg="white",height=2,width=10,command=eti)
        eti_btn.place(x=325,y=450)

        tip_btn = tk.Button(root,text="Tips",fg="black",bg="white",height=2,width=10,command=tips)
        tip_btn.place(x=540,y=450)


    logo_label.destroy()
    instruction_label.destroy()
    rule_btn.destroy()
    eti_btn.destroy()
    tip_btn.destroy()
    root.geometry("1000x650")
    eti_txt = tk.Text(root,bg="black",fg="white",borderwidth=0,width=71,height=100)
    eti_txt.place(x=50,y=50)
    theetiquettes = """Lanes are the divisions of road through paint that can be found on wide roads like highways. On a 3-lane road (left lane, middle lane, right lane) where we exclude the emergency lane, all car drivers should be on the middle lane for most of the journey. The left lane should be left for only trucks, buses, or any slow vehicles. The right lane should only be used when you need to overtake someone in front of you. Say you're in the middle lane, driving behind a person who is slow and you want to go faster than them. You'd take the right lane, speed up, then change back to the middle lane once you've overtook the person that was previously in front of you. So, in short, the right lane is only for the fast vehicles. This same rule applies on any road no matter the amount of lanes. The faster you get, the more of the right side you are on.\n\nTo switch lanes properly, first you must check all your mirrors to see if there is anyone behind you that is close to you. If there isn't, go switch lanes right away or turn on blinkers and then switch if you want (Its optional). If there is someone, then turn on your blinkers that indicate the corresponding direction (If you are planning to change to a right lane, then turn on your right blinker) and finally switch to that other lane. Blinkers and mirrors are essential in avoiding accidents, so always remember to use them. Because Indonesians tend to forget using their blinkers, mirrors, and lanes properly, traffic and accidents form easily. However, they aren't the only things needed to avoid accidents. We suggest that you should practice on having a larger vision than just the cars in front of you as you are not the only individual on this planet. This can be done through mirrors yet again, and just looking left and right. This larger vision then can also be applied when arriving from a smaller road to a bigger road. You first look left and right to see if there is anyone, and if there is you'll have to wait until its empty before going onto the road.\n\nAnother thing that is important but obvious is your self control. Make sure that you always remember to follow these etiquettes and not get angry at others for not doing so. You should also not get frustrated when others overtake you as it is a completely normal action that provides convenience to the drivers, and does no harm to you."""
    eti_txt.insert(tk.END,theetiquettes)
    global overtake
    overtake = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\overtake1.png")
    overtake_label = tk.Label(root,image=overtake,bg="gray")
    overtake_label.place(x=650,y=175)
    back = tk.Button(root,text="<- Back",fg="black",bg="white",command=home)
    back.place(x=1,y=1)

def tips():
    def home():
        root.geometry("700x550")
        back.destroy()
        tipsi_label.destroy()
        tip_txt.destroy()
        global logo
        global rule_btn
        global eti_btn
        global tip_btn
        global logo_label
        global instruction_label
        logo = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\drivelogo.png")
        logo_label = tk.Label(root,image=logo,borderwidth=0)
        logo_label.place(x=190,y=105)

        instruction_label = tk.Label(root,text="Select a course to review",fg="white",bg="black")
        instruction_label.place(x=250,y=350)
        instruction_label.configure(font=("Calibri",15,BOLD))
        rule_btn = tk.Button(root,text="Rules",fg="black",bg="white",height=2,width=10,command=rules)
        rule_btn.place(x=100,y=450)

        eti_btn = tk.Button(root,text="Etiquettes",fg="black",bg="white",height=2,width=10,command=eti)
        eti_btn.place(x=325,y=450)

        tip_btn = tk.Button(root,text="Tips",fg="black",bg="white",height=2,width=10,command=tips)
        tip_btn.place(x=540,y=450)

    logo_label.destroy()
    instruction_label.destroy()
    rule_btn.destroy()
    eti_btn.destroy()
    tip_btn.destroy()
    root.geometry("700x600")
    tip_txt = tk.Text(root,bg="black",fg="white",borderwidth=0,width=71,height=100)
    tip_txt.place(x=50,y=50)
    thetips = """1. Have an increased vision on the road so you can anticipate other people's actions and reduce the amount of brakes you do, making it more convenient.\n\n2. Always use your mirrors to know your full surroundings.\n\n3. Increase your gear everytime your speed increases by 20km/h to save gas or bensin.\ne.g. 20km/h = Gear 1, 40km/h = Gear 2, etc.\n\n3. Kepp all the documents in your car (like your dashboard) in case you ever need it in urgent matters.\n\n4. Always ensure your tire pressure is at its correct amount (Pressure can be found somewhere in the car)."""
    tip_txt.insert(tk.END,thetips)
    global tipsi
    tipsi = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\tips.png")
    tipsi_label = tk.Label(root,image=tipsi,bg="gray")
    tipsi_label.place(x=210,y=320)
    back = tk.Button(root,text="<- Back",fg="black",bg="white",command=home)
    back.place(x=1,y=1)

# Buttons

rule_btn = tk.Button(root,text="Rules",fg="black",bg="white",height=2,width=10,command=rules)
rule_btn.place(x=100,y=450)

eti_btn = tk.Button(root,text="Etiquettes",fg="black",bg="white",height=2,width=10,command=eti)
eti_btn.place(x=325,y=450)

tip_btn = tk.Button(root,text="Tips",fg="black",bg="white",height=2,width=10,command=tips)
tip_btn.place(x=540,y=450)

root.mainloop()