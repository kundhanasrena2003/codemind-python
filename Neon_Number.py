n=int(input())
m=n*n
s=0
while(m>0):
    r=m%10
    s+=r
    m=m//10
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")