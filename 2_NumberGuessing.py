import tkinter as tk
from tkinter import messagebox
import random

low = 1
high = 100
theGuess = random.randint(low, high)
attempts = 0

def check(event=None):
    global attempts, theGuess
    guess = int(entry.get())
    attempts += 1
    
    if guess < theGuess:
        tk.messagebox.showinfo("Incorrect", "The guess is too low")
    elif guess > theGuess:
        tk.messagebox.showinfo("Incorrect", "The guess is too high")
    else:
        tk.messagebox.showinfo("Correct", f"{theGuess} was correct! It took you {attempts} attempts.")

root = tk.Tk()
root.title("Number Guessing Game")

label = tk.Label(root, text="Guess the number between 1 and 100: ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Guess", command=check)
button.pack()

root.bind('<Return>', check)

root.mainloop()