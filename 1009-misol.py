def bitwiseComplement(n):
    arr=[]
    if n==0:
        return 1
    while n>=1:
        arr.append(n%2)
        n=n//2
    arr1=arr[::-1]
    for i in range(len(arr1)):
        if arr1[i]==0:
            arr1[i]=1
        else:
            arr1[i]=0
    s=0
    j=0
    while len(arr1)>j:
            if arr1[j]==1:
                arr1.pop(j)
                x=len(arr1)
                s+=2**x
            elif arr1[j]==0:
                arr1.pop(j)
                s+=0
            else:
                j+=1
    return s


print(bitwiseComplement(7))