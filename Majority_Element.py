x=int(input())
x=str(x)
l=list(map(int,input().split()))
z=0
s=[]
for i in l:
    if i not in s:
        s.append(i)
        k=l.count(i)
        if(k>=z):
            z=k
            h=i
    else:
        pass
print(h)