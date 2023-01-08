import tkinter as tk

root = tk.Tk()
root.title("Driving Quiz")

# Starting Question
q1 = tk.Label(root,text="You're arriving from a smaller road to a bigger road at a turn. What is the right procedure at this moment?", fg="black")
q1.pack()

# Functions
score = 0

def right1():
    global score
    score = score + 100
    q1.destroy()
    a1.destroy()
    a2.destroy()
    print(score)

    def right2():
        global score
        score = score + 100
        q2.destroy()
        a3.destroy()
        a4.destroy()
        e1.destroy()
        print(score)

        def right3():
            global score
            score = score + 100
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right4():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()

            def wrong4():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right4)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong4)
            a8.pack()
        
        def wrong3():
            global score
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right4():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()

            def wrong4():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right4)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong4)
            a8.pack()

        q3 = tk.Label(root,text="What do you use the blinker lights for?",fg="black")
        q3.pack()
        a5 = tk.Button(root,text="To show that you will be going in a specific direction wthin 60km", fg="black",bg="white", command=wrong3)
        a5.pack()
        a6 = tk.Button(root,text="To indicate that you're making a turn or lane change", fg="black",bg="white", command=right3)
        a6.pack()
    
    def wrong2():
        global score
        q2.destroy()
        a3.destroy()
        a4.destroy()
        e1.destroy()
        print(score)

        def right3():
            global score
            score = score + 100
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right4():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            def wrong4():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right4)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong4)
            a8.pack()
            
        def wrong3():
            global score
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right4():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            def wrong4():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right5():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong5():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right5)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong5)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right4)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong4)
            a8.pack()

        q3 = tk.Label(root,text="What do you use the blinker lights for?",fg="black")
        q3.pack()
        a5 = tk.Button(root,text="To show that you will be going in a specific direction wthin 60km", fg="black",bg="white", command=wrong3)
        a5.pack()
        a6 = tk.Button(root,text="To indicate that you're making a turn or lane change", fg="black",bg="white", command=right3)
        a6.pack()
    

    q2 = tk.Label(root,text="You're driving in your car at 70 km/h on a 3-lane highway (Left lane, Middle lane, Right lane) along with trucks and cars. In front of you, there is no one to be seen for another 500m. Which lane should you be driving on at this current moment?",fg="black")
    q2.pack()
    a3 = tk.Button(root,text="Middle Lane", fg="black",bg="white", command=right2)
    a3.pack()
    a4 = tk.Button(root,text="Left Lane", fg="black",bg="white", command=wrong2)
    a4.pack()
    e1 = tk.Button(root,text="Right Lane", fg="black",bg="white", command=wrong2)
    e1.pack()



def wrong1():
    global score
    q1.destroy()
    a1.destroy()
    a2.destroy()
    print(score)
    
    def wrong22():
        global score
        q2.destroy()
        a3.destroy()
        a4.destroy()
        e1.destroy()
        print(score)

        def right33():
            global score
            score = score + 100
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right44():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()

            def wrong44():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right44)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong44)
            a8.pack()
        
        def wrong33():
            global score
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right44():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()

            def wrong44():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right44)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong44)
            a8.pack()

        q3 = tk.Label(root,text="What do you use the blinker lights for?",fg="black")
        q3.pack()
        a5 = tk.Button(root,text="To show that you will be going in a specific direction wthin 60km", fg="black",bg="white", command=wrong33)
        a5.pack()
        a6 = tk.Button(root,text="To indicate that you're making a turn or lane change", fg="black",bg="white", command=right33)
        a6.pack()

    def right22():
        global score
        score = score + 100
        q2.destroy()
        a3.destroy()
        a4.destroy()
        e1.destroy()
        print(score)

        def right33():
            global score
            score = score + 100
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right44():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()

            def wrong44():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

                def right55():
                    global score
                    score = score + 100
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                def wrong55():
                    global score
                    q5.destroy()
                    a9.destroy()
                    a10.destroy()
                    print(score)
                
                q5 = tk.Label(root,text="What is the correct way to use your mirrors for driving?",fg="black")
                q5.pack()
                a9 = tk.Button(root,text="To check if someone is behind you", fg="black",bg="white", command=right55)
                a9.pack()
                a10 = tk.Button(root,text="To check the status of your passengers at the back", fg="black",bg="white", command=wrong55)
                a10.pack()
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right44)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong44)
            a8.pack()
        
        def wrong33():
            global score
            q3.destroy()
            a5.destroy()
            a6.destroy()
            print(score)

            def right44():
                global score
                score = score + 100
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)

            def wrong44():
                global score
                q4.destroy()
                a7.destroy()
                a8.destroy()
                print(score)
            
            q4 = tk.Label(root,text="Which is the proper sequence assuming no one is behind you?",fg="black")
            q4.pack()
            a7 = tk.Button(root,text="Check the mirror, turn on the blinker lights, and then change lanes", fg="black",bg="white", command=right44)
            a7.pack()
            a8 = tk.Button(root,text="Turn on the blinker lights, check the mirror, and then change lanes", fg="black",bg="white", command=wrong44)
            a8.pack()

        q3 = tk.Label(root,text="What do you use the blinker lights for?",fg="black")
        q3.pack()
        a5 = tk.Button(root,text="To show that you will be going in a specific direction wthin 60km", fg="black",bg="white", command=wrong33)
        a5.pack()
        a6 = tk.Button(root,text="To indicate that you're making a turn or lane change", fg="black",bg="white", command=right33)
        a6.pack()

    q2 = tk.Label(root,text="You're driving in your car at 70 km/h on a 3-lane highway (Left lane, Middle lane, Right lane) along with trucks and cars. In front of you, there is no one to be seen for another 500m. Which lane should you be driving on at this current moment?",fg="black")
    q2.pack()
    a3 = tk.Button(root,text="Middle Lane", fg="black",bg="white", command=right22)
    a3.pack()
    a4 = tk.Button(root,text="Left Lane", fg="black",bg="white", command=wrong22)
    a4.pack()
    e1 = tk.Button(root,text="Right Lane", fg="black",bg="white", command=wrong22)
    e1.pack()


# Answers
a1 = tk.Button(root,text="Look left and right before going into the bigger road. You must make sure that there are no other vehicles near you before you can turn into the bigger road, no matter what.", fg="black",bg="white", command=right1)
a1.pack()

a2 = tk.Button(root,text="Look left and right before going into the bigger road. If there is no vehicle, you turn onto the road and continue. If there is a vehicle, you let it stop by going in front of them before they reach you, and then continuing onto the bigger road.", fg="black",bg="white", command=wrong1)
a2.pack()


root.geometry("1300x120")
root.mainloop()