def runningSum(nums):
    def getResult():
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            yield s

    return getResult()