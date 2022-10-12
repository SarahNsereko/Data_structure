#Sorted array 
#Array should be atleast fairly uniform or else the performance will decrease and more steps will be needed 
#The time complexity depends on the uniformity of data 
def interpolationsearch(array,high,low,target):

#recursive approach 

    if (low<=high and target>=array[low] and target<=array[high]): 
            pos=(low+((target-array[low])*(high-low))// (array[high]-array[low]))#To calculate the index of a wanted value
            if array[pos]==target:
                return pos

            elif array[pos]<target:
                return interpolationsearch(array,pos+1,high,target) #if it is less increase the value of pos by 1 and recalculate
            elif array[pos]>target:
                return interpolationsearch(array,low,pos-1,target)#if it is more decrease the value by 1 and recalculate pos
    return -1 #if not found


array=[1,3,5,7,9,11,13,15,17,19,21,29]
n=len(array)
high=n-1
low=0
target=29
   
print(interpolationsearch(array,high,low,target))

