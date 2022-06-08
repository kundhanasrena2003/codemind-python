x=int(input())
for i in range(x):
    for j in range(x):
        if i==j or i==x-j-1:
            print("x",end="")
        else:
            print("0",end="")
    print()