#Leetcode Problem working through arrays
#Given an array of integers A sorted in non-decreaseing order,
#return an array of the squares of each number
#also sorted non-decreasing order

def sortedsquares(self,a):
    squares = [] 
    for x in a: 
      squares.append(x*x)
      squares.sort()
    return squares 

#This is not the most optimized solution 
#Will come back to this to figure it out later


