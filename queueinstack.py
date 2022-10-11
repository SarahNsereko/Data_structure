from queue import LifoQueue
stack=LifoQueue(maxsize=6)
print(stack.qsize())#qsize helps us get the size of the stack
stack.put('s')
stack.put('a')
stack.put('r')
stack.put('a')
stack.put('h')
print("Is the stack full: ",stack.full())#Stack.full helps to tell us the array size 
print("What is the size of the stack: ",stack.qsize())
stack.get()
print(stack.get())
stack.get()
print(stack.get())

