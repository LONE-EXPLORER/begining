def co(i , j):
    if(i==j):
        return(1)
    elif(i > j):
        i = i-j
        return(co(i , j) + 1)
    elif(j > i):
        j = j-i
        return(co(j , i) + 1)

p = int(input())
q = int(input())
r = int(input())
s = int(input())
n = 0
for i in range(p , q+1):
    for j in range(r , s+1):
        n += co(i , j)
print(n)
