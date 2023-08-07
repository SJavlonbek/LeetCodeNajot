def kidsWithCandies(candies, extraCandies):
    
    def getResult():
        x=max(candies)
        list1=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=x:
                yield list1.append(True)
            else:
                yield list1.append(False)