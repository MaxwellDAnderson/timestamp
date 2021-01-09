from tkinter import *
import datetime


root = Tk()
root.title("Timestamp")
root.geometry("600x400")
text = Text(root, height=400, width=600)

a = datetime.datetime.utcnow()
b = str(a)
c = " UTC: ---START OF DOCUMENT---"
d = b + c

text.insert(END, d)


def stamp(event):
    e = datetime.datetime.utcnow()
    f = str(e) + " UTC: "
    g = "\n"
    h = g + g + f
    i = h.removesuffix('\n')

    text.insert(END, i)


text.bind("<Return>", stamp)
text.pack()

root.mainloop()
