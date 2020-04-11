#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program: 8 Then, the output should be:40320


#Using recursion to solve this 
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1) 

