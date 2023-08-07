def uniqueOccurrences(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    return len(count.values()) == len(set(count.values()))

print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # True
print(uniqueOccurrences([1, 2]))  # False
print(uniqueOccurrences([4, 0, 2, -5, -4]))  # False
