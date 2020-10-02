l = int(input())
f = str(input())
m = str(input())
s = t
a  = 0
while (s != a or m != ""):
    c =0
    if f[0] == m[0]:
        f = f[1:]
        m = m[1:]
        a += 1
    else:
        c += 1
        x = m[0]
        m = m[1:]
        x = m + x
        if(c == len(m)):
            break

print(l - a)
