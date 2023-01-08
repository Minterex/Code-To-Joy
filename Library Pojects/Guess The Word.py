import tkinter as tk
import sys

counter = 0

root = tk.Tk()
root.title("Guess The Word")
root.geometry("500x500")
root.configure(bg="#363534")

frame = tk.Frame(root,bg="#1e1e1f", width=450,height=450)
frame.place(x=25,y=25)

# WORD INPUT

def on_focus_in(event):
    if event.widget.get() == 'Input your word here':
        event.widget.delete('0', 'end')
        event.widget.config(fg='white')

def on_focus_out(event):
    if event.widget.get() == '':
        event.widget.insert(0, 'Input your word here')
        event.widget.config(fg='gray')

word_input = tk.Entry(frame,bg="#21211f",fg="white", width=50)
word_input.insert(0, 'Input your word here')
word_input.bind('<FocusIn>', on_focus_in)
word_input.bind('<FocusOut>', on_focus_out)
word_input.place(x=75,y=170)

# STARTING THE GAME

def get_word():
    global secret_word
    secret_word = word_input.get()
    submit.destroy()
    word_input.destroy()

    def on_focus_in(event):
        if event.widget.get() == 'How many guesses should be given?':
            event.widget.delete('0', 'end')
            event.widget.config(fg='white')

    def on_focus_out(event):
        if event.widget.get() == '':
            event.widget.insert(0, 'How many guesses should be given?')
            event.widget.config(fg='gray')

    guesses_input = tk.Entry(frame,bg="#21211f",fg="white", width=50)
    guesses_input.insert(0, 'How many guesses should be given?')
    guesses_input.bind('<FocusIn>', on_focus_in)
    guesses_input.bind('<FocusOut>', on_focus_out)
    guesses_input.place(x=75,y=170)

    def get_guesses():
        global guesses
        guesses = int(guesses_input.get())
        submit_guesses.destroy()
        guesses_input.destroy()

        def on_focus_in(event):
            if event.widget.get() == 'Guess the word!':
                event.widget.delete('0', 'end')
                event.widget.config(fg='white')

        def on_focus_out(event):
            if event.widget.get() == '':
                event.widget.insert(0, 'Guess the word!')
                event.widget.config(fg='gray')

        answer_input = tk.Entry(frame,bg="#21211f",fg="white", width=50)
        answer_input.insert(0, 'Guess the word!')
        answer_input.bind('<FocusIn>', on_focus_in)
        answer_input.bind('<FocusOut>', on_focus_out)
        answer_input.place(x=75,y=170)

        how_many_guesses = tk.Label(frame,fg="white",bg="#1e1e1f",text=f"You have {guesses} guesses!")
        how_many_guesses.place(x=170,y=300)

        def answer_detection():
            global answers
            answers = answer_input.get()
            if answers == secret_word:
                answer_input.destroy()
                submit_answers.destroy()
                how_many_guesses.destroy()
                frame.configure(bg="teal")
                you_win = tk.Label(frame,fg="black",font=("times", 20),text="YOU WON",bg="teal")
                you_win.place(x=155,y=200)

        def guesses_counter():
            global counter
            counter = counter + 1
            if counter == guesses:
                answer_input.destroy()
                submit_answers.destroy()
                how_many_guesses.destroy()
                frame.configure(bg="red")
                you_win = tk.Label(frame,fg="black",font=("times", 20),text="YOU LOST",bg="red")
                you_win.place(x=155,y=200)
            print(counter)

        def multi_commands():
            guesses_counter()
            answer_detection()

        submit_answers = tk.Button(frame,bg="#21519e",fg="white",text="Submit Your Word", command=multi_commands)
        submit_answers.place(x=170,y=250)


    submit_guesses = tk.Button(frame,bg="#21519e",fg="white",text="Submit Your Word", command=get_guesses)
    submit_guesses.place(x=170,y=250)




submit = tk.Button(frame,bg="#21519e",fg="white",text="Submit Your Word", command=get_word)
submit.place(x=170,y=250)

root.mainloop()
