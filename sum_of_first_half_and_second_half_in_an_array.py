n=int(input())
a=list(map(int,input().split()))
print(sum(a[:n//2]))
print(sum(a[n//2:]))