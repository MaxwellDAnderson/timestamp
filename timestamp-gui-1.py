from tkinter import *
import datetime
import subprocess as sub
from subprocess import Popen, PIPE


root = Tk()
root.title("Timestamp")
root.geometry("600x400")


a = datetime.datetime.utcnow()
b = str(a)
c = "UTC: "
d = "---START OF DOCUMENT---"
e = b + " " + c + d

# print(b, c, d)

text = Text(root, height=400, width=600)
text.insert(END, e)


def stamp(event):
    f = datetime.datetime.utcnow()
    g = str(f)
    h = "UTC: "
    i = g + " " + h
    j = "\n"
    k = j + j + i
    m = k.removesuffix('\n')
    # myLabel = Label(root, text=j)
    # print(i)
    text.insert(END, m)
    # sys.stdout.write.myText(i)


text.bind("<Return>", stamp)
text.pack()

root.mainloop()
