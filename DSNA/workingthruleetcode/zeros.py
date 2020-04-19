#Leet code array problem 
#Given a fixed length array arr of integers, duplicate each occurence of zero
#shifting the remianing elements to the right 

def duplicateZeroes(self,arr):
    x = 0 
    while x < len(arr):
        if arr[x] == 0:
            arr.pop()
            arr.insert(x+1,0)
            x = x + 1
        x = x + 1