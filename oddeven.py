List=[]
odd=0
even=0
for i in range(1,10):
    if i%2==0:
        even+=1
    else:
        odd+=1
    List.append(i)

print(List)
print(odd)
print(even)
