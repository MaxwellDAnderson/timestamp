import datetime

a = datetime.datetime.utcnow()
b = str(a)
c = "UTC: "
d = "---START OF DOCUMENT---"
e = b + " " + c

print(b, c, d)

# firstInput = input(e)

endDoc = "\\\\\\"

while True:
    f = datetime.datetime.utcnow()
    g = str(f)
    h = "UTC: "
    i = g + " " + h
    n = input(i)
    if n != endDoc:
        continue
    # print(g, h)
    else:
        break

j = datetime.datetime.utcnow()
k = str(j)
m = "UTC: ---END OF DOCUMENT---"
print(k, m)

'''

x = datetime.datetime.utcnow()
y = "UTC:"
z = str(x)

a = z + " " + y
print(x, y, "---START OF DOCUMENT---")
userInput = input(a)


if userInput.casefold() == "yes":
    print(x, y)
else:
    print(x, y, "Okay, goodbye!")
'''

# input("Would you like to know the date and time?")
# print(x)
