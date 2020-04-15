#From Udemy Complete Python Coding BootCamp

#Write a function that computes the volume
#of a sphere given its radius

def vol(rad):
    return ((4/3) * 3.14 * (rad**3))


#Write a function that checks whether a number
#is in a given range (inclusive high or low)

def ran_check(num, low, high):
    if num in range (low,high):
        return True
    else:
        return False

#Write a python function that takes in a list
#and returns a new list with unique elements 

def unique(l):
    new = []
    for x in l:
        if x not in x:
            x.append(new)
    return x 

#These are other practice problems below onward

#Write a function to convert from Kilos to lbs

def kilolb(x):
    return x * 2.20462

