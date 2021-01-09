from tkinter import *
import datetime


root = Tk()
root.title("Timestamp")
root.geometry("600x400")
text = Text(root, height=400, width=600)

text.tag_config("timestamp", foreground="blue")

a = datetime.datetime.utcnow()
b = str(a)
c = " UTC: "
p = "---START OF DOCUMENT---"
d = b + c + p + "\n" + b + c


text.insert(END, d, "timestamp")


def stamp(event):
    e = datetime.datetime.utcnow()
    f = str(e) + " UTC: "
    g = "\n"
    h = g + g + f
    i = h.removesuffix('\n')
    text.insert(END, i, "timestamp")


def end(event):
    j = datetime.datetime.utcnow()
    k = str(j) + " UTC: ---END OF DOCUMENT---"
    m = "\n"
    n = m + m + k
    o = n
    text.insert(END, o, "timestamp")


text.bind("<Return>", stamp)
text.focus_set()
text.bind("<backslash><backslash><backslash>", end)
text.pack()

root.mainloop()
