x=int(input())
z=0
k=1
temp=x
while(x):
    d=x%10
    x=x//10
    z=z+d
while(temp):
    d=temp%10
    temp=temp//10
    k=k*d
if(k==z):
    print("Spy Number")
else:
    print("Not Spy Number")