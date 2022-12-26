import os
import sys
import subprocess

print()
print()
print()
print()
print("Starting a round...")

i = 1
secret_word = str(input("What is your secret word: "))
guess_limit = int(input("How many guesses can be performed: "))
guess_count = 0
guess = ""

while i <= 50:
    print(i)
    i = i + 1

while guess != secret_word and guess_count < guess_limit:
    guess = input("Guess the secret word: ")
    guess_count = guess_count + 1
    print(f"{guess_limit - guess_count} guesses left")

if guess == secret_word:
    print("You WON and guessed " + secret_word + " correctly within the guess limit!")
else:
    print("You LOST and ran out of guesses. The word was " + secret_word)

subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
#^^^ code to restart the program

