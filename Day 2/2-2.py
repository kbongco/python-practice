#List Less than ten 
#Found on practicepython.org
#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less = []
for x in a:
    if x < 5:
        less.append(x)
print(less)