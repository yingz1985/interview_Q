#Find sum of unique values in the list, if a value is not unique, increment until it is 
def getUniqueUserIdSum(arr):
    sum_ = 0
    count  = {}

    newarr = []
    for num in arr:
        temp = num
        while temp in count: #
            temp = temp+1
        count[temp]=1
        newarr.append(temp)
    
    for num in newarr:
        sum_+=num
    return sum_
        
print(getUniqueUserIdSum([1,2,2]))
