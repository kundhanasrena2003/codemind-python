def prime(a):
    if a<2:
        return 0
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return 0
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==1:
        print(i)