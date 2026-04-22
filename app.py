import requests
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Random Cat Facts!")
window.geometry("1000x500")
window.resizable(False, False)

prompt = tk.Label(window, text="Number of facts:", font=("Arial", 16))
prompt.pack(pady=50)

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=0)

def catfacts():
    amount=entry.get()
    if not amount:
        print("Enter a valid number!") 
    else:
        response = requests.get(f"https://meowfacts.herokuapp.com/?count={amount}")
        if response.status_code != 200:
            print("Error fetching data!")
            return None
        fact = response.json()
        print(fact['data'])

catfacts_button = tk.Button(window, text="Learn More About Cats!", font=("Arial", 20), command=catfacts, relief="raised")
catfacts_button.pack(pady=80)

def meow():
    print("Meow")

meow_button = tk.Button(window, text="Meow", font=("Arial", 14), command=meow, relief="raised")
meow_button.pack(pady=5)

image = Image.open("my_photo.jpg")
photo = ImageTk.PhotoImage(image)
label = tk.Label(window, image=photo)
label.pack(pady=20)

window.mainloop() 
 
