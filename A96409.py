def binary_search(array,target):
    
    start=0
    
    end=len(array)-1
    
    n=len(array)
        
    for i in range(len(array)):
            
        for j in range(len(array)-i-1):
                
            if array[j]>array[j+1]:
                    
                array[j],array[j+1]=array[j+1],array[j]
                    
                print(array)
                    
    while start<=end:
        
        
                    mid=int((start+end)//2)
                    
                    if target==array[mid]:
                        return mid
                    
                    elif target<array[mid]:
                        end=mid-1
                        
                    else:
                        beginning=mid+1 
                                      
array=[8,9,8,7]

target=7
print(binary_search(array,target))


def bubblesort(arr):
    n=len(arr)
    for i in range (n):
        sort_status=False#If it is not sorted
        for j in range (0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr [j+1]=temp
                sort_status=True

        if not sort_status:#if it is sorted
            break

    return arr
arr=[6,8,2,4,2,1]
print(bubblesort(arr))


#Optimization of mergesort
array = [2,6,8,1,8,55,48]

def mergeSort(arr):

    j = 0
    i = 1

    if len(arr)<= 1:
        return arr
    
    while i < len(arr):
        if(arr[i] < arr[i - 1]):
            j = 1
        i += 1

    if (not j) :
        return arr
    else :
        mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)

    print(len (arr))
    print(left)
    print(right)
    
    return merge(left,right)

def merge(a,b):
    sortedArray = []

    x=0
    y=0

    len_a = len(a)
    len_b = len(b)

    while x < len_a and y< len_b:
        if a[x] <= b[y]:
            sortedArray.append(a[x])
            x += 1
        else:
            sortedArray.append(b[y])
            y += 1
    while x < len_a:
        sortedArray.append(a[x])
        x += 1
    while y < len_b:
        sortedArray.append(b[y])
        y += 1

    return sortedArray
print(mergeSort(array))