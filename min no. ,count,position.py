def findmin(n,data):
    s,c=data[0],0
    for i in data:
        if s==i:
            c+=1
        if s>i:
            s=i
            c=1
    ind=[s,c]
    for i in range(n):
        if s==data[i]:
            ind.append(i)
    return ind
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)
