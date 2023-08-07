def relativeSortArray(arr1, arr2):
    arr3 = []
    arr4 = []
    
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr2[i] == arr1[j]:
                arr3.append(arr1[j])
    
    for j in range(len(arr1)):
        if arr1[j] not in arr2:
            arr4.append(arr1[j])
    
    arr4 = sorted(arr4)
    arr3.extend(arr4)
    
    return arr3

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relativeSortArray(arr1, arr2))
