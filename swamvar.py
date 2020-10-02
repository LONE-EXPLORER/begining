n = int(input())
b = str(input())
g = str(input())

k , t = n , n

for j in range(len(b)):
    for i in range(len(g)):
        if(b[0] == g[0]):
            k -= 1
            b = b[1:]
            g = g[1:]
        else:
            temp = g[0]
            g = g[1:] + temp
    if(t == k):
        break
    else:
        t = k

print(k)