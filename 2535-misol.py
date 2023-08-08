def differenceOfSum(nums):
    x=sum(nums)
    z=0
    for i in range(len(nums)):
        while nums[i]>9:
            z+=nums[i]%10
            nums[i]=nums[i]//10
        if nums[i]<=9:
            z+=nums[i]

    return x-z

print(differenceOfSum([1,15,6,3]))