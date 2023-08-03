def missingNumber(nums):
    for i in range(len(nums)+1):
        if i not in nums:
            return i
    return i+1
nums=[3,0,1]
print(missingNumber(nums))