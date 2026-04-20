import requests
import tkinter as tk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("500x500")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:",font=("Arial", 14))
prompt.pack(pady=20)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=20)

def catfacts():
    amount=entry.get()
    response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    fact = response.json()
    print(fact['data'])
    enumerate(fact['data'])

catfacts_button = tk.Button(window, text="Learn More About Cats!",font=("Arial", 20),command=catfacts, relief="raised")
catfacts_button.pack(pady=100)

window.mainloop()

""" def say_hello():
    print("Hello there!")

window = tk.Tk()
window.title("Button Example")
# Create the button
my_button = tk.Button(
window, # parent container
text="Say Hello", # label text
command=say_hello, # function to call when clicked
font=("Arial", 16), # nice big font
bg="lightblue", # background color
fg="black", # text color
relief="raised", # gives it a 3D look
padx=10, pady=5 # padding around the text

)
my_button.pack(pady=20) # place it on the window
window.mainloop() """