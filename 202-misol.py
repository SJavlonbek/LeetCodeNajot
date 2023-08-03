def isHappy(n):
    while n>0:
        n=sum(int(x)*int(x) for x in str(n))
        if n==1 or n==7:
            return True
        elif n<=9:
            return False