#Print sum of numbers
array=[2,3,1,2,3]
def sum(array,N):
    if N<=0:
        return 0
    else:
        return sum(array,N-1)+array[N-1]
N=len(array)


print(sum(array,N))

#Print stars
def stars (i):
    if i< 9:
        print("*"*i)#Print i as many times as that number 
        i+=1
        stars(i) 
i=0
stars(i)