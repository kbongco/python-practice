#Given two numbers, write a function that 
#returns the sum if the product is greater than 1000




def twonums(x,y):
    if x * y > 1000:
        return x + y 
    else:
        return x * y