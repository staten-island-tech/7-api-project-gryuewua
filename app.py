import requests
import tkinter as tk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("1000x600")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:", font=("Arial", 20))
prompt.pack(pady=40)

entry = tk.Entry(window, font=("Arial", 14), width=20)
entry.pack(pady=0)

def catfacts():
    amount=entry.get()
    if not amount or amount != int:
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

answer = tk.Label(window, text="", font=("Arial", 16),wraplength=900)
answer.pack(pady=20,fill="both",expand=True)

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
selfdestruct_button.place(x=450, y=550)

window.mainloop() 