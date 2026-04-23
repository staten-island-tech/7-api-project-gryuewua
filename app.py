import requests
import tkinter as tk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("1000x600")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:", font=("Arial", 20))
prompt.pack(pady=30)

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
answer.pack(pady=100,fill="both",expand=True)

window.mainloop() 