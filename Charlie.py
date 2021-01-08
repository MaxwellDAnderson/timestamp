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
    n = input(i)
    if n != endDoc:
        continue
    else:
        break

j = datetime.datetime.utcnow()
k = str(j)
m = "UTC: ---END OF DOCUMENT---"
print(k, m)
