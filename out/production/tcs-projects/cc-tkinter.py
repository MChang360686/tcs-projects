import tkinter as tk
from tkinter import messagebox
import time

GAME_FILE = 'cclicker-at-home.txt'

upgrades = {'click': 0, 'grandma': 0, 'factory': 0, 'mine': 0}

def load_data():
    try:
        with open(GAME_FILE, 'r') as file:
            data = file.readlines()

            for i in range(0, len(data)):
                if i == 0:
                    print(data[i])

    except FileNotFoundError:
        open(GAME_FILE, "w").close()

def click(last_time):
    curr_time = int(time.perf_counter())
    cookies = (time * (curr_time - last_time)) + (click + (upgrades[1] * 5) + (upgrades[2] * 50) + (upgrades[2] * 100))
    return cookies    

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

add_button = tk.Button(root, text="Click", font=("Arial", 12), command=click)
add_button.pack(pady=5)