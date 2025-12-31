from tkinter import *
import requests

def get_quote():
    try:
        response = requests.get("https://api.kanye.rest")
        response.raise_for_status()
        quote = response.json()["quote"]
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException:
        canvas.itemconfig(quote_text, text="Failed to get quote. Try again.")

window = Tk()
window.title("Somebody Says")
window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=500)
bg_image = PhotoImage(file="a4531c951cc6f36db591f1a8c529cf40-removebg-preview.png")
canvas.create_image(250, 250, image=bg_image)
quote_text = canvas.create_text(250, 250, text="Click the button for a quote", width=250, font=("Times New Roman", 20), fill="black")
canvas.grid(column=1, row=1)

button_image = PhotoImage(file="b43a892e3f68c50a5b7ce996aa41a1af-removebg-preview (1).png")
button = Button(image=button_image, highlightthickness=0, command=get_quote)
button.grid(column=1, row=2)

window.mainloop()
