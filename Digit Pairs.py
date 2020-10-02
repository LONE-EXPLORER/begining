n = int(input())
l = list(map(int , input().split()))
su = 0
arr = []
for i in range(n):
    r = []
    s = 0
    k = l[i]
    while(k != 0):
       r.append(k%10)
       k = k//10
    s = (max(r) * 11) + (min(r) * 7)
    s = s % 100
    arr.append(s)
even  , odd =[] , []
for i in range(len(arr)):
    if(i%2 == 0):
        even.append(arr[i])
    else:
        odd.append(arr[i])
for i in range(1 , 10):
    count = 0
    for j in range(len(even)):
        if(even[j]//10 == i):
            count += 1
    if(count == 2):
        su += 1
    elif(count >2):
        su += 2
    count = 0
    for j in range(len(odd)):
        if(odd[j]//10 == i):
            count += 1
    if (count == 2):
        su += 1
    elif (count > 2):
        su += 2
print(su)



