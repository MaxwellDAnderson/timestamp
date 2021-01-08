import datetime

a = datetime.datetime.utcnow()
b = str(a)
c = "UTC: "
d = "---START OF DOCUMENT---"
e = b + " " + c

print(b, c, d)

endDoc = "\\\\\\"

while True:
    f = datetime.datetime.utcnow()
    g = str(f)
    h = "UTC: "
    i = g + " " + h
    j = input(i)
    if j != endDoc:
        continue
    else:
        break

k = datetime.datetime.utcnow()
m = str(k)
n = "UTC: ---END OF DOCUMENT---"
print(m, n)
