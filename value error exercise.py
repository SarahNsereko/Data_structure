



def squareroot(x):
   # This is because you cant have square roots of negative numbers
    try:
         import math
         
         result= math.sqrt(x)
         print("The square root is ",result)
    except ValueError:
        print("You have entered a wrong number  ")
        
      
    except TypeError:
        print("You entered too many arguments") 
        
x=int(input("Enter one positive number"))
squareroot(x)
    
    