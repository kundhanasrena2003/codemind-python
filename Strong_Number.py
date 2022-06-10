x=int(input())
temp=x
k=1
s=0
while x>0:
    d=x%10
    x=x//10
    for i in range(d,0,-1):
        k=k*i
    s=s+k
    k=1
if(s==temp):
    print("The number {0} is a strong number".format(temp))
else:
    print("The number {0} is not a strong number".format(temp))