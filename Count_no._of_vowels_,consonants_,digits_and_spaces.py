x=input()
c=0
k=0
z=0
s=0
for i in range(len(x)):
    if x[i] in 'aeiouAEIOU':
        c+=1
    elif x[i] in '1234567890':
        k+=1
    elif x[i] in ' ':
        s+=1
    else:
        z+=1
print("Vowels:",c)
print("Consonants:",z)
print("Digits:",k)
print("White spaces:",s)