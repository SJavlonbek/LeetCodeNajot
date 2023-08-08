def sumOfMultiples(n):
    s=0
    for i in range(1,n+1):
        if i%3==0 or i%5==0 or i%7==0:
            s+=i
    return s

print(sumOfMultiples(7))

# def sumOfMultiples(n):
#     def getRes():
#         s=0
#         for i in range(1,n+1):
#             if i%3==0 or i%5==0 or i%7==0:
#                 s+=1
#         yield s
#     return getRes()

# print(sumOfMultiples(7))