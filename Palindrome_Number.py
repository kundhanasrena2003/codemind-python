x=int(input())
k=0
for i in range(x):
    z=int(input())
    temp=z
    while z:
        d=z%10
        z=z//10
        k=k*10+d
    if(temp==k):
        print("True")
    else:
        print("False")
    k=0