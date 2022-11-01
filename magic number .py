#Program to 
print("Hi ! Welcome to my guess the number game!")
print("Enter an integer please")
number=(int(input()))
secret_number= 59
while number!=secret_number:
     print ("Ha ha! You're stuck in my loop!")
     print ("Try again")
     number=(int(input()))
if number == secret_number:
         print("Well done, muggle! You are free now.")
