import requests
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("1000x700")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:", font=("Arial", 20))
prompt.pack(pady=40)

entry = tk.Entry(window, font=("Arial", 14), width=20)
entry.pack(pady=0)

def catfacts():
    amount=entry.get()
    if not amount:
        answer.config(text="Enter a valid number!") 
    else:
        response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            answer.config(text="Error fetching data!") 
            return None
        fact = response.json()
        answer.config(text=f"{fact['data']}")

catfacts_button = tk.Button(window, text="Learn More About Cats!", font=("Arial", 20), command=catfacts, relief="raised")
catfacts_button.pack(pady=40)

def meow():
    answer.config(text="Meow")

meow_button = tk.Button(window, text="Meow", font=("Arial", 20), command=meow, relief="raised")
meow_button.pack(pady=0)

canvas = tk.Canvas(window, height=20, width=400)
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
frame = ttk.Frame(canvas)
canvas.create_window((500, 200), window=frame,anchor="center")
scrollbar.pack(side="right", fill="y")
canvas.pack(pady=20,side="top",fill="both", expand=True)

answer = ttk.Label(frame, text="", font=("Arial", 16),wraplength=900)
answer.pack(pady=0,fill=tk.BOTH ,expand=True)

def update_scroll_region(event):    
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", update_scroll_region)

explosion = tk.PhotoImage(file="boom.png")

def boom():
    answer.config(text="Bro why did you do that")
    window.after(1000, boomaction)
    window.after(1500, window.destroy)

def boomaction():
    boom=tk.Label(window)
    boom.place(x=0, y=-200)
    boom.config(image=explosion) 
    
selfdestruct_button = tk.Button(window, text="DO NOT PRESS", font=("Arial", 10), command=boom, relief="raised")
selfdestruct_button.pack(pady=20)

window.mainloop() 