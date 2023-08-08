# def smallerNumbersThanCurrent(nums):
    
#     nums2=[]
#     for i in range(len(nums)):
#         x=nums[i]
#         s=0
#         for j in range(len(nums)):
#             if x>nums[j]:
#                 s+=1
#         nums2.append(s)
#     return nums2

# print(smallerNumbersThanCurrent([8,1,2,2,3]))

def smallerNumbersThanCurrent(nums):
    
    def getResult():
        nums2=[]
        for i in range(len(nums)):
            x=nums[i]
            s=0
            for j in range(len(nums)):
                if x>nums[j]:
                    s+=1
        yield nums2.append(s)
    return getResult()

print(smallerNumbersThanCurrent([8,1,2,2,3]))