array=[2,1,1,4,7,2,8,6]

def bubble(array ):
    n=len(array)-1
    sorted=False
    while not sorted:#it will stop when sorting status=True
        sorted=True
        for i in range(0,n):
            if array[i]>array[i+1]:
                sorted=False#if the element is larger than the one on its right then its not sorted 
                array[i],array[i+1]=array[i+1],array[i]
    return array

print(bubble(array))