def getConcatenation(nums):
    ans = nums.copy()
    for i in nums:
        ans.append(i)
    return ans

a = [1, 2, 3]
print(getConcatenation(a))
