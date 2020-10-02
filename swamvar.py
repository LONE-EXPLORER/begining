n = int(input())
b = str(input())
g = str(input())

a , t = n , n

for j in range(len(b)):
    for i in range(len(g)):
        if(b[0] == g[0]):
            a -= 1
            b = b[1:]
            g = g[1:]
        else:
            temp = g[0]
            g = g[1:] + temp
    if(t == a):
        break
    else:
        t = a

print(a)
