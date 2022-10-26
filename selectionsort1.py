def selectionsort(array):
    
    for i in range(0,len(array)-1):#Loop through and get the min value in the entire array
        minvalue = i#make it first element 

        for j in range(i+1,len(array)):#increase the pointer position by one and then look for the next minimum value 
            if array[j] < array[minvalue]:#if a value less than original minvale is found
                minvalue=j#new min value should be at position j
                
            if minvalue != i:#since min value!=i ,switch
                array[minvalue],array[i]=array[i],array[minvalue]#value at new minvalue position j and value at old min value i should switch 
    return array 
array=[8,6,7,4,3]

print(selectionsort(array))