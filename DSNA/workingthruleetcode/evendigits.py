#Working through leetcode arrays
#Find numbers with even number of digits

def findNumbers(self,nums):
    count = 0 

    for x in nums:
        if len(str(x)) % 2 == 0:
            count += 1
    
    return count