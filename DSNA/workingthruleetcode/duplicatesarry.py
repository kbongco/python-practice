#Working Thru Leetcode
#given a sorted array nums remove the duplicates in place
#such as that each elements appear only once

def remove(nums):
    x = 0 
    for i in range(1,len(nums)):
        if nums[x] != nums [i]:
            x += 1
            nums[x] = nums[i]
    return x + 1 