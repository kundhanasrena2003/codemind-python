n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if sum(arr)%2==0:
        print("1")
        break
    else:
        print("0")
        break