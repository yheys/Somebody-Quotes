from tkinter import *
import requests


def get_quots():

    quot=requests.get(url="https://api.kanye.rest")
    quot.raise_for_status()
    qoute=quot.json()["quote"]
    canvas.itemconfig(qout_text, text=qoute)








window=Tk()
window.title("Somebody says")
window.config(padx=50,pady=50)

canvas=Canvas(width=500,height=500)
p1=PhotoImage(file="a4531c951cc6f36db591f1a8c529cf40-removebg-preview.png")
canvas.create_image(250,250, image=p1)
qout_text=canvas.create_text(200,260,text="the text is here",width=250,font=("New Times Roman",20))
canvas.grid(column=1,row=1)


p2=PhotoImage(file="b43a892e3f68c50a5b7ce996aa41a1af-removebg-preview (1).png")
button=Button(image=p2,width=150,height=200,highlightthickness=0,command=get_quots)
button.grid(column=1,row=2)





window.mainloop()