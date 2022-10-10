import math
def jumpsearch(array,target,length):
    step=int(math.sqrt(length)) #find the number of jumps
    math.ceil(step)
    print("The jump size is ",step)
    last_index=0
    while array[int(min(step,length)-1)] < target:#If the value at the end is less than the target last index=step and then increment by jump size
     
        last_index=step
       
        print("Last index= ",last_index)
        step+=math.sqrt(length)
        if last_index>=length:
            return -1
# linearsearch 

    while array[int(last_index)]< target:
        last_index=last_index+1#if value at the last index is less than the target increase the index by one

        if last_index==min(step,length):#If it has reached the end
            return -1

    if array[int(last_index)]==target:
        return last_index
    return -1


array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
target=15
length=len(array)
wantedindex=jumpsearch(array,target,length)
print("The value your looking for is at  ", wantedindex)
