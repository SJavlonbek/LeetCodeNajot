def restoreString(s, indices):
    x = ''
    for i in range(len(indices)):
        x += s[indices[i]]
    return x

restored_string = restoreString("codeleet", [4, 5, 6, 7, 0, 1,2, 3])
print(restored_string)