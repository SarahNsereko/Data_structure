b = int(input())
m = input().strip().split(' ')
reversearr = m[::-1]
space=""

for i in range(b):
    space = space+ str(reversearr[i]) + " "
    
print(space)