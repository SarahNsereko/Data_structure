#This code reverses a string and prints them as one word
a="Happy Coding"
g=[]
for i in a:
    print(i)
    g.append(i)

print(g)
f=g[::-1]
print(f)
k=""
h=k.join(f)
print(h)
