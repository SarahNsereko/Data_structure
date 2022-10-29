array=[1 ,3,9,0,2]
max=array[0]
min=array[0]

for i in range(1,len(array)):
    if array[i]<min:
        min=array[i]

    if array[i]>max:
        max=array[i]

print(max)
print(min)

