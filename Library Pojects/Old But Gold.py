import tkinter as tk
from tkinter.font import BOLD
import webbrowser

root = tk.Tk()
root.geometry("700x500")
root.title("Old But Gold | Adopt A Dog")
root.configure(bg="#1a222e")

#Functions
def start():

    def notjeff():

        def notjolie():

            def notfin():

                def notmelly():

                    def notoreo():

                        def nottimmy():

                            def notbarney():

                                def notbarry():

                                    def notbesse():

                                        def notwillie():
                                            willie_label.destroy()
                                            willie_name.destroy()
                                            not_interested_willie.destroy()
                                            interested_willie.destroy()

                                        besse_label.destroy()
                                        not_interested_besse.destroy()
                                        interested_besse.destroy()
                                        besse_name.destroy()

                                        #Willie
                                        global willie_img
                                        willie_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Willie - Old But Gold.png")
                                        willie_label = tk.Label(root,image=willie_img,borderwidth=0)
                                        willie_label.place(x=185,y=50)
                                        willie_name = tk.Label(root,text="Willie",bg="#1a222e",fg="white")
                                        willie_name.place(x=377,y=450)
                                        not_interested_willie = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notwillie)
                                        not_interested_willie.place(x=300,y=500)
                                        interested_willie = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/adopt-willie/#main"))
                                        interested_willie.place(x=400,y=500)

                                    barry_label.destroy()
                                    not_interested_barry.destroy()
                                    interested_barry.destroy()
                                    barry_name.destroy()

                                    #Besse
                                    global besse_img
                                    besse_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Besse - Old But Gold.png")
                                    besse_label = tk.Label(root,image=besse_img,borderwidth=0)
                                    besse_label.place(x=185,y=50)
                                    besse_name = tk.Label(root,text="Besse",bg="#1a222e",fg="white")
                                    besse_name.place(x=377,y=450)
                                    not_interested_besse = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notbesse)
                                    not_interested_besse.place(x=300,y=500)
                                    interested_besse = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/adopt-besse/#main"))
                                    interested_besse.place(x=400,y=500)

                                barney_label.destroy()
                                not_interested_barney.destroy()
                                interested_barney.destroy()
                                barney_name.destroy()

                                #Barry
                                global barry_img
                                barry_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Barry - Old But Gold.png")
                                barry_label = tk.Label(root,image=barry_img,borderwidth=0)
                                barry_label.place(x=185,y=50)
                                barry_name = tk.Label(root,text="Barry",bg="#1a222e",fg="white")
                                barry_name.place(x=377,y=450)
                                not_interested_barry = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notbarry)
                                not_interested_barry.place(x=300,y=500)
                                interested_barry = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/thumbnail_adopt-barry/#main"))
                                interested_barry.place(x=400,y=500)


                            timmy_label.destroy()
                            not_interested_timmy.destroy()
                            interested_timmy.destroy()
                            timmy_name.destroy()

                            #Barney
                            global barney_img
                            barney_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Barney - Old But Gold.png")
                            barney_label = tk.Label(root,image=barney_img,borderwidth=0)
                            barney_label.place(x=185,y=50)
                            barney_name = tk.Label(root,text="Barney",bg="#1a222e",fg="white")
                            barney_name.place(x=377,y=450)
                            not_interested_barney = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notbarney)
                            not_interested_barney.place(x=300,y=500)
                            interested_barney = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/thumbnail_adopt-barney/#main"))
                            interested_barney.place(x=400,y=500)

                        oreo_label.destroy()
                        not_interested_oreo.destroy()
                        interested_oreo.destroy()
                        oreo_name.destroy()

                        #Timmy
                        global timmy_img
                        timmy_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Timmy - Old But Gold.png")
                        timmy_label = tk.Label(root,image=timmy_img,borderwidth=0)
                        timmy_label.place(x=185,y=50)
                        timmy_name = tk.Label(root,text="Timmy",bg="#1a222e",fg="white")
                        timmy_name.place(x=377,y=450)
                        not_interested_timmy = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=nottimmy)
                        not_interested_timmy.place(x=300,y=500)
                        interested_timmy = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/timmy-adopt/#main"))
                        interested_timmy.place(x=400,y=500)

                    melly_label.destroy()
                    not_interested_melly.destroy()
                    interested_melly.destroy()
                    melly_name.destroy()

                    #Oreo
                    global oreo_img
                    oreo_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Oreo - Old But Gold.png")
                    oreo_label = tk.Label(root,image=oreo_img,borderwidth=0)
                    oreo_label.place(x=185,y=50)
                    oreo_name = tk.Label(root,text="Oreo",bg="#1a222e",fg="white")
                    oreo_name.place(x=377,y=450)
                    not_interested_oreo = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notoreo)
                    not_interested_oreo.place(x=300,y=500)
                    interested_oreo = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/image1-copy/#main"))
                    interested_oreo.place(x=400,y=500)


                fin_label.destroy()
                not_interested_fin.destroy()
                interested_fin.destroy()
                fin_name.destroy()

                #Melly
                global melly_img
                melly_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Melly - Old But Gold.png")
                melly_label = tk.Label(root,image=melly_img,borderwidth=0)
                melly_label.place(x=185,y=50)
                melly_name = tk.Label(root,text="Melly",bg="#1a222e",fg="white")
                melly_name.place(x=377,y=450)
                not_interested_melly = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notmelly)
                not_interested_melly.place(x=300,y=500)
                interested_melly = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/melly-adopt/#main"))
                interested_melly.place(x=400,y=500)


            jolie_label.destroy()
            not_interested_jolie.destroy()
            interested_jolie.destroy()
            jolie_name.destroy()

            #Fin
            global fin_img
            fin_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Fin - Old But Gold.png")
            fin_label = tk.Label(root,image=fin_img,borderwidth=0)
            fin_label.place(x=185,y=50)
            fin_name = tk.Label(root,text="Fin",bg="#1a222e",fg="white")
            fin_name.place(x=377,y=450)
            not_interested_fin = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notfin)
            not_interested_fin.place(x=300,y=500)
            interested_fin = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/adopt-fin-2/#main"))
            interested_fin.place(x=400,y=500)

        jeff_label.destroy()
        not_interested_jeff.destroy()
        interested_jeff.destroy()
        jeff_name.destroy()

        #Jolie
        global jolie_img
        jolie_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Jolie - Old But Gold.png")
        jolie_label = tk.Label(root,image=jolie_img,borderwidth=0)
        jolie_label.place(x=185,y=50)
        jolie_name = tk.Label(root,text="Jolie",bg="#1a222e",fg="white")
        jolie_name.place(x=377,y=450)
        not_interested_jolie = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notjolie)
        not_interested_jolie.place(x=300,y=500)
        interested_jolie = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/adopt-jolie/#main"))
        interested_jolie.place(x=400,y=500)

    root.geometry("775x600")
    logolabel.destroy()
    ready.destroy()
    yes.destroy()
    donationinstructions.destroy()

    #Jeff
    global jeff_img
    jeff_img = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\Jeff - Old But Gold.png")
    jeff_label = tk.Label(root,image=jeff_img,borderwidth=0)
    jeff_label.place(x=185,y=50)
    jeff_name = tk.Label(root,text="Jeff",bg="#1a222e",fg="white")
    jeff_name.place(x=377,y=450)
    not_interested_jeff = tk.Button(root,text="Next",bg="red",fg="black",width=10,command=notjeff)
    not_interested_jeff.place(x=300,y=500)
    interested_jeff = tk.Button(root,text="I'm Interested",bg="white",fg="black",width=10,command=lambda: webbrowser.open("https://www.jakartaanimalaid.com/adopt/adoptadog/jeff-adopt-2/#main"))
    interested_jeff.place(x=400,y=500)



#Home Page
logo = tk.PhotoImage(file=r"C:\Users\ACER\Code Projects\VS Code\Code To Joy\CodeToJoy Resources\oldbutgoldlogo.png")
logolabel = tk.Label(root,image=logo,bg="#1a222e")
logolabel.place(x=174,y=70)

ready = tk.Label(root,text="Are you ready to adopt poor old dogs?",fg="white",bg="#1a222e")
ready.configure(font=("Calibri",15,BOLD))
ready.place(x=180,y=300)

yes = tk.Button(root,text="I am ready",bg="white",fg="black",width=10,command=start)
yes.place(x=305,y=360)

donationinstructions = tk.Text(root,bg="#1a222e",fg="white",borderwidth=0,width=80)
donationinstructions.place(x=24,y=410)
theinstructions = """If you are willing to adopt any of these beautiful dogs, visit the JAAN website that is provided and follow the instructions on the website as all of these dogs                           were saved by the JAAN."""
donationinstructions.insert(tk.END,theinstructions)


root.mainloop()