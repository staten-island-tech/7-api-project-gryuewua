import requests
import tkinter as tk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("500x500")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:",font=("Arial", 16))
prompt.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=20)

def catfacts():
    amount=entry.get()
    if not amount:
        print("Enter a number!") 
    else:
        response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        fact = response.json()
        print(fact['data'])

catfacts_button = tk.Button(window, text="Learn More About Cats!",font=("Arial", 20),command=catfacts, relief="raised")
catfacts_button.pack(pady=100)

def meow():
    print("Meow")

meow_button = tk.Button(window, text = "Meow", font = ("Arial", 14), command = meow, relief = "raised")
meow_button.pack(pady=20)

window.mainloop()