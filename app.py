import requests
import tkinter as tk

def catfacts(amount):
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    fact = response.json()
    return fact

print(catfacts("5"))



window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("500x500")
window.resizable(False, False)

prompt = tk.Label(window, text="Type your message below:",
font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

catfacts_button = tk.Button(window, text="Reverse Message!",font=("Arial", 14),command=catfacts)

