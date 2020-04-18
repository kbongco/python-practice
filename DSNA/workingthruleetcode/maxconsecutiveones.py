#LeetCode Problems
#Max consecutive ones 

def MaxConsecutiveOnes(self,nums):
    longest = 0 
    highest = 0 

    for x in nums: 
        if x == 1:
            count += 1
        else:
            if count > highest:
                highest = count
            count = 0 
    return max(highest,count)

#Explaining how to do this
#We are trying to find the number of 
#consecutive ones
#Set a counter - > count would equal 0 
#set a loop to go through the nums which
#would be the list 
#Since we are also looking for the longest list
#There should also be a counter for the longest
#Next we do another statement to check if the count is longer than the list 